/* Single source of truth for company details. Fill these in; leave empty until verified. */
const SITE = {
  demo: true,          // demo mode: forms show a labeled demo confirmation when no backend is connected. Set false for launch.
  name: "HVAC Demo",            // [[TBC: company name]]
  phone: "2125550100",           // digits only, e.g. "5555550100" (US)
  textCapable: true,  // true only if the number can receive texts
  license: "000000 (demo)",         // [[TBC: license no. and state]]
  supabaseUrl: "",     // [[TBC: https://YOUR-PROJECT.supabase.co]]
  supabaseKey: "",     // [[TBC: publishable / anon key (public by design)]]
  unitsServiced: 8400,  // demo figure
  serviceZips: ["10001","10002","10003","10004","10005"]      // [[TBC: ZIP codes actually served]], e.g. ["60601","60602"]
};
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];

/* Fill company details; until configured, call/text buttons jump to the contact section. */
const fmt = d => d.length === 10 ? `(${d.slice(0,3)}) ${d.slice(3,6)}-${d.slice(6)}` : d;
if (SITE.name) $$("[data-site=name]").forEach(e => e.textContent = SITE.name);
if (SITE.license) $$("[data-site=license]").forEach(e => { e.textContent = "License " + SITE.license; e.classList.remove("tbc"); });
if (SITE.phone) $$("[data-site=phone]").forEach(e => { e.textContent = fmt(SITE.phone); e.classList.remove("tbc"); });
$$("[data-call]").forEach(a => { a.href = SITE.phone ? "tel:+1" + SITE.phone : "#contact"; });
$$("[data-text]").forEach(a => {
  if (SITE.phone && SITE.textCapable) a.href = "sms:+1" + SITE.phone;
  else { a.href = "#contact"; }
});
$$("[data-year]").forEach(e => e.textContent = new Date().getFullYear());

/* Mobile menu */
const mb = $(".menu-btn"), ul = $("#menu");
mb.addEventListener("click", () => { const o = ul.classList.toggle("open"); mb.setAttribute("aria-expanded", o); });
$$("#menu a").forEach(a => a.addEventListener("click", () => { ul.classList.remove("open"); mb.setAttribute("aria-expanded", false); }));

/* ZIP checker: uses only the owner-supplied list; never guesses coverage */
$("#zipForm")?.addEventListener("submit", e => {
  e.preventDefault();
  const z = $("#zip").value.trim(), out = $("#zipMsg");
  if (!/^\d{5}$/.test(z)) { out.textContent = "Enter a 5-digit ZIP code."; return; }
  if (!SITE.serviceZips.length) { out.textContent = "Our service-area list isn't published yet. Call us and we'll confirm coverage."; return; }
  out.textContent = SITE.serviceZips.includes(z) ? `We serve ${z}. Request a quote or schedule service below.` : `${z} is outside our listed service area. Call us and we'll see what we can do.`;
});

/* System explorer: tabs with keyboard support */
const tabs = $$(".tabs [role=tab]"), panels = $$(".panel");
const pick = i => tabs.forEach((t, n) => { const on = n === i; t.setAttribute("aria-selected", on); t.tabIndex = on ? 0 : -1; panels[n].hidden = !on; });
tabs.forEach((t, i) => {
  t.addEventListener("click", () => pick(i));
  t.addEventListener("keydown", e => {
    if (!["ArrowDown","ArrowUp","ArrowLeft","ArrowRight"].includes(e.key)) return;
    e.preventDefault(); const n = (i + (/Down|Right/.test(e.key) ? 1 : -1) + tabs.length) % tabs.length; pick(n); tabs[n].focus();
  });
});

/* Quote form: inserts a row in Supabase; success is shown only when Supabase confirms it */
const qf = $("#quoteForm");
qf?.addEventListener("submit", async e => {
  e.preventDefault();
  const out = $("#quoteMsg"), btn = qf.querySelector("[type=submit]"), d = Object.fromEntries(new FormData(qf));
  if (d.website) { location.href = "thank-you.html"; return; } // honeypot: bots get a fake success
  if (!(d.name || "").trim() || (d.phone || "").replace(/\D/g, "").length < 10 || !/^\d{5}$/.test(d.zip || "")) { out.textContent = "Please enter your name, a 10-digit phone number and a 5-digit ZIP code."; return; }
  if (!SITE.supabaseUrl || !SITE.supabaseKey) { out.textContent = SITE.demo ? "✓ Demo mode: this is where your request would be sent. Nothing was saved." : "This form isn't connected yet, so nothing was sent. Please call or text us."; if (SITE.demo) qf.reset(); return; }
  const row = { name: d.name.trim(), phone: d.phone.trim(), email: (d.email || "").trim() || null, zip: d.zip, property_type: d.type, service: d.service,
    urgency: d.urgency, details: (d.details || "").slice(0, 2000), text_ok: !!qf.elements.textok?.checked, source_page: location.pathname.slice(0, 100) };
  const headers = { apikey: SITE.supabaseKey, "Content-Type": "application/json", Prefer: "return=minimal" };
  if (SITE.supabaseKey.startsWith("eyJ")) headers.Authorization = "Bearer " + SITE.supabaseKey; // legacy JWT anon key
  btn.disabled = true; out.textContent = "Sending…";
  try {
    const r = await fetch(SITE.supabaseUrl.replace(/\/$/, "") + "/rest/v1/quote_requests", { method: "POST", headers, body: JSON.stringify(row) });
    if (r.ok) { location.href = "thank-you.html"; return; }
  } catch {}
  out.textContent = "We couldn't send your request. Please call or text us instead."; btn.disabled = false;
});

/* Reveal once on scroll (skipped for reduced motion) */
if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion:reduce)").matches) {
  const io = new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } }), { threshold: .12 });
  $$(".reveal").forEach(el => io.observe(el));
} else $$(".reveal").forEach(el => el.classList.add("in"));

/* Project filter */
$$(".chips button").forEach(b => b.addEventListener("click", () => {
  $$(".chips button").forEach(x => x.setAttribute("aria-pressed", x === b));
  $$(".proj").forEach(c => c.hidden = b.dataset.f !== "all" && c.dataset.cat !== b.dataset.f);
}));
