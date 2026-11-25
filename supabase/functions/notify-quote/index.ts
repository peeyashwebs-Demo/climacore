// Optional: emails the owner when a row is inserted. Wire it to a Database Webhook (INSERT on quote_requests).
// Secrets: WEBHOOK_SECRET, RESEND_API_KEY, QUOTE_TO_EMAIL, QUOTE_FROM_EMAIL. Deploy with --no-verify-jwt (the secret header protects it).
Deno.serve(async (req) => {
  if (req.headers.get("x-webhook-secret") !== Deno.env.get("WEBHOOK_SECRET")) return new Response("Forbidden", { status: 403 });
  const { record: r } = await req.json();
  if (!r) return new Response("No record", { status: 400 });
  const one = (v: unknown) => String(v ?? "").replace(/[\r\n]+/g, " ");
  const text = [`Name: ${one(r.name)}`, `Phone: ${one(r.phone)}`, `Email: ${one(r.email) || "(none)"}`, `ZIP: ${one(r.zip)}`,
    `Property: ${one(r.property_type)}`, `Service: ${one(r.service)}`, `Urgency: ${one(r.urgency)}`,
    `OK to text (box ticked): ${r.text_ok ? "yes" : "no"}`, `Submitted: ${one(r.created_at)}`, `Page: ${one(r.source_page)}`, "", "Details:", String(r.details ?? "(none)")].join("\n");
  const res = await fetch("https://api.resend.com/emails", { method: "POST",
    headers: { Authorization: `Bearer ${Deno.env.get("RESEND_API_KEY")}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from: Deno.env.get("QUOTE_FROM_EMAIL"), to: [Deno.env.get("QUOTE_TO_EMAIL")],
      ...(r.email && { reply_to: r.email }), subject: `New quote request (${one(r.urgency)}): ${one(r.service)}, ${one(r.zip)}`, text }) });
  return new Response(res.ok ? "ok" : "email failed", { status: res.ok ? 200 : 502 });
});
