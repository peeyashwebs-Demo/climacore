-- Run in Supabase > SQL Editor. Visitors (anon) can ONLY insert, and only these columns.
create table if not exists public.quote_requests (
  id            uuid primary key default gen_random_uuid(),
  created_at    timestamptz not null default now(),
  status        text not null default 'new' check (status in ('new','contacted','visit_scheduled','quoted','won','lost','spam')),
  name          text not null check (char_length(name) between 2 and 100),
  phone         text not null check (phone ~ '^[0-9()+.\- ]{10,20}$'),
  email         text check (email is null or (char_length(email) <= 120 and email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$')),
  zip           text not null check (zip ~ '^[0-9]{5}$'),
  property_type text check (char_length(property_type) <= 60),
  service       text check (char_length(service) <= 60),
  urgency       text check (char_length(urgency) <= 60),
  details       text check (char_length(details) <= 2000),
  text_ok       boolean not null default false,
  source_page   text check (char_length(source_page) <= 100)
);

alter table public.quote_requests enable row level security;
revoke all on table public.quote_requests from anon, authenticated;
grant insert (name, phone, email, zip, property_type, service, urgency, details, text_ok, source_page)
  on public.quote_requests to anon;
drop policy if exists "visitors can submit requests" on public.quote_requests;
create policy "visitors can submit requests" on public.quote_requests for insert to anon with check (true);
-- No select/update/delete policy for anon: only signed-in dashboard users / the service role can read leads.

-- Flood cap: refuse new rows if 30+ arrived in the last 10 minutes (best-effort spam protection).
create or replace function public.quote_flood_cap() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if (select count(*) from public.quote_requests where created_at > now() - interval '10 minutes') >= 30 then
    raise exception 'Too many requests, try again later';
  end if;
  return new;
end $$;
drop trigger if exists quote_flood_cap on public.quote_requests;
create trigger quote_flood_cap before insert on public.quote_requests for each row execute function public.quote_flood_cap();

-- Newsletter signups: visitors can only add an email.
create table if not exists public.newsletter_signups (
  id uuid primary key default gen_random_uuid(), created_at timestamptz not null default now(),
  email text not null unique check (char_length(email) <= 120 and email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'));
alter table public.newsletter_signups enable row level security;
revoke all on table public.newsletter_signups from anon, authenticated;
grant insert (email) on public.newsletter_signups to anon;
drop policy if exists "visitors can subscribe" on public.newsletter_signups;
create policy "visitors can subscribe" on public.newsletter_signups for insert to anon with check (true);
