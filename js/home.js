/* Homepage interactions. Needs js/main.js loaded first (SITE, $, $$). */
const RM = matchMedia("(prefers-reduced-motion:reduce)").matches;

/* Hero: clickable hotspots + demo temperature control */
const info = { filter: "Filtration: captures dust and particles. The right filter depends on the system's airflow capacity.",
  air: "Airflow: supply direction and ductwork design shape comfort, noise and efficiency.",
  ctrl: "Controls: schedules, smart thermostats and zoning match conditioning to how a space is used." };
$$(".hot").forEach(b => b.addEventListener("click", () => { $$(".hot").forEach(x => x.setAttribute("aria-pressed", x === b)); $("#cap").textContent = info[b.dataset.k]; }));
let temp = 24; const scr = $("#scr");
$$("[data-t]").forEach(b => b.addEventListener("click", () => { temp = Math.min(30, Math.max(16, temp + +b.dataset.t)); scr.textContent = temp + "°"; }));

/* Statement: words light up as you scroll */
const st = $("#stmt"); st.innerHTML = st.textContent.trim().split(/\s+/).map(w => `<span class="w">${w}</span>`).join(" ");
const ws = $$(".w", st);
const paint = () => { const r = st.getBoundingClientRect(), vh = innerHeight, p = Math.min(1, Math.max(0, (vh * .85 - r.top) / (r.height + vh * .35)));
  ws.forEach((w, i) => w.classList.toggle("on", RM || i < p * ws.length)); };
addEventListener("scroll", paint, { passive: true }); paint();

/* Count-up: only animates a real number from SITE.unitsServiced */
const cu = $("#units"), n = Number(SITE.unitsServiced);
if (n > 0) { cu.classList.remove("tbc"); let t0; const step = t => { t0 ??= t; const k = Math.min(1, (t - t0) / 1400); cu.textContent = Math.round(n * k).toLocaleString("en-US"); if (k < 1) requestAnimationFrame(step); };
  new IntersectionObserver((e, o) => { if (e[0].isIntersecting) { RM ? cu.textContent = n.toLocaleString("en-US") : requestAnimationFrame(step); o.disconnect(); } }).observe(cu); }

/* 3D coverflow: buttons, dots, keys, swipe */
const sls = $$(".sl"), dots = $("#dots"); let cur = 0;
dots.innerHTML = sls.map((_, i) => `<button aria-label="Show slide ${i + 1}"></button>`).join("");
const titles = sls.map(s => $("h3", s).textContent);
function cf() { const N = sls.length;
  sls.forEach((s, i) => { let d = i - cur; if (d > N / 2) d -= N; if (d < -N / 2) d += N; const a = Math.abs(d);
    s.style.transform = `translateX(${d * 58}%) translateZ(${-a * 140}px) rotateY(${d * -26}deg) scale(${d ? .88 : 1})`;
    s.style.opacity = a > 2 ? 0 : 1 - a * .25; s.style.zIndex = 10 - a; s.style.pointerEvents = a > 2 ? "none" : "auto"; s.setAttribute("aria-hidden", d !== 0); });
  $$("button", dots).forEach((b, i) => b.setAttribute("aria-current", i === cur)); $("#cfcap").textContent = titles[cur]; }
const go = i => { cur = (i + sls.length) % sls.length; cf(); };
$("#prev").onclick = () => go(cur - 1); $("#next").onclick = () => go(cur + 1);
$$("button", dots).forEach((b, i) => b.onclick = () => go(i)); sls.forEach((s, i) => s.onclick = () => go(i));
const cfEl = $(".cf"); cfEl.tabIndex = 0; cfEl.addEventListener("keydown", e => { if (e.key === "ArrowRight") go(cur + 1); if (e.key === "ArrowLeft") go(cur - 1); });
let x0 = null; cfEl.addEventListener("pointerdown", e => x0 = e.clientX);
cfEl.addEventListener("pointerup", e => { if (x0 !== null && Math.abs(e.clientX - x0) > 40) go(cur + (e.clientX < x0 ? 1 : -1)); x0 = null; }); cf();

/* Visit wheel: click a step; auto-advances unless reduced motion */
const steps = [["Start the conversation", "Call, text or send the form."], ["Onsite assessment", "We look at the space, the system and your goals."],
  ["Service plan review", "We walk through findings and options in writing."], ["Ongoing system care", "Handover and planned maintenance."]];
const nodes = $$(".wheel>button"); let wi = 0, timer;
const setW = i => { wi = i; nodes.forEach((b, k) => { const a = ((k - i) * 90 - 90) * Math.PI / 180; b.style.left = 50 + 50 * Math.cos(a) + "%"; b.style.top = 50 + 50 * Math.sin(a) + "%";
  b.setAttribute("aria-pressed", k === i); b.setAttribute("aria-label", `Step ${k + 1}: ${steps[k][0]}`); }); $("#wt").textContent = steps[i][0]; $("#wd").textContent = steps[i][1]; };
nodes.forEach((b, i) => b.addEventListener("click", () => { clearInterval(timer); setW(i); })); setW(0);
if (!RM) timer = setInterval(() => setW((wi + 1) % 4), 5000);

/* Reviews slider with numbered pager (placeholders until real reviews are supplied) */
const rs = $$(".rv figure"), rp = $("#rp"); let ri = 0;
rp.innerHTML = rs.map((_, k) => `<button aria-label="Review ${k + 1}">${k + 1}</button>`).join("");
const showR = i => { ri = (i + rs.length) % rs.length; rs.forEach((f, k) => f.hidden = k !== ri); $$("button", rp).forEach((b, k) => b.setAttribute("aria-current", k === ri)); };
$$("button", rp).forEach((b, k) => b.onclick = () => showR(k)); $("#rprev").onclick = () => showR(ri - 1); $("#rnext").onclick = () => showR(ri + 1); showR(0);

/* Team carousel */
const tm = $("#team"); $("#tprev").onclick = () => tm.scrollBy({ left: -330, behavior: RM ? "auto" : "smooth" }); $("#tnext").onclick = () => tm.scrollBy({ left: 330, behavior: RM ? "auto" : "smooth" });

/* Projects: vertical scroll drives the horizontal track (desktop, motion allowed) */
const pin = $("#projects"), trk = $("#trk");
function pinSet() { if (innerWidth <= 820 || RM) { trk.style.transform = ""; pin.style.height = ""; return; }
  const dist = Math.max(0, trk.scrollWidth - innerWidth + 60); pin.style.height = innerHeight + dist + "px";
  const p = Math.min(1, Math.max(0, -pin.getBoundingClientRect().top / (pin.offsetHeight - innerHeight || 1))); trk.style.transform = `translateX(${-p * dist}px)`; }
addEventListener("scroll", pinSet, { passive: true }); addEventListener("resize", pinSet); pinSet();

/* Newsletter: saves to Supabase only when connected */
$("#nl")?.addEventListener("submit", async e => { e.preventDefault(); const out = $("#nlMsg"), em = String(new FormData(e.target).get("email") || "").trim();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em)) { out.textContent = "Please enter a valid email address."; return; }
  if (!SITE.supabaseUrl || !SITE.supabaseKey) { out.textContent = SITE.demo ? "✓ Demo mode: you would be subscribed here. Nothing was saved." : "Signup isn't connected yet, so nothing was saved."; return; }
  const h = { apikey: SITE.supabaseKey, "Content-Type": "application/json", Prefer: "return=minimal" }; if (SITE.supabaseKey.startsWith("eyJ")) h.Authorization = "Bearer " + SITE.supabaseKey;
  try { const r = await fetch(SITE.supabaseUrl.replace(/\/$/, "") + "/rest/v1/newsletter_signups", { method: "POST", headers: h, body: JSON.stringify({ email: em }) });
    out.textContent = r.ok || r.status === 409 ? "Thanks, you're subscribed." : "We couldn't subscribe you. Please try again later."; } catch { out.textContent = "We couldn't subscribe you. Please try again later."; } });
