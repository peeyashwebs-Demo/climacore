/* Homepage interactions. Needs js/main.js loaded first. */
const RM = matchMedia("(prefers-reduced-motion:reduce)").matches;

/* Hero: clickable hotspots + temperature control */
const info = { filter: "Filtration: captures dust and particles. The right filter depends on the system's airflow capacity.",
  air: "Airflow: supply direction and ductwork design shape comfort, noise and efficiency.",
  ctrl: "Controls: schedules and smart thermostats match cooling to how a space is used." };
$$(".hot").forEach(b => b.addEventListener("click", () => { $$(".hot").forEach(x => x.setAttribute("aria-pressed", x === b)); $("#cap").textContent = info[b.dataset.k]; }));
let temp = 24; const scr = $("#scr");
$$("[data-t]").forEach(b => b.addEventListener("click", () => { temp = Math.min(30, Math.max(16, temp + +b.dataset.t)); scr.textContent = temp + "°"; }));

/* Statement: words light up as you scroll */
const st = $("#stmt"); st.innerHTML = st.textContent.trim().split(/\s+/).map(w => `<span class="w">${w}</span>`).join(" ");
const ws = $$(".w", st);
const paint = () => { const r = st.getBoundingClientRect(), vh = innerHeight, p = Math.min(1, Math.max(0, (vh * .85 - r.top) / (r.height + vh * .35)));
  ws.forEach((w, i) => w.classList.toggle("on", RM || i < p * ws.length)); };
addEventListener("scroll", paint, { passive: true }); paint();

/* County check: lists the counties Climacore publishes on its Contact page */
$("#cty").addEventListener("submit", e => { e.preventDefault(); const c = $("#county").value;
  $("#ctyMsg").textContent = c ? `Yes, we serve ${c} County. Book online or call us any time.` : "Please select your county first."; });

/* 3D coverflow: buttons, dots, keys, swipe */
const sls = $$(".sl"), dots = $("#dots"); let cur = 0;
dots.innerHTML = sls.map((_, i) => `<button aria-label="Show slide ${i + 1}"></button>`).join("");
const titles = sls.map(s => $("h3", s).textContent);
function cf() { const N = sls.length;
  sls.forEach((s, i) => { let d = i - cur; if (d > N / 2) d -= N; if (d < -N / 2) d += N; const a = Math.abs(d);
    s.style.transform = `translateX(${d * 58}%) translateZ(${-a * 140}px) rotateY(${d * -26}deg) scale(${d ? .88 : 1})`;
    s.style.opacity = a > 2 ? 0 : 1 - a * .25; s.style.zIndex = 10 - a; s.style.pointerEvents = a > 2 ? "none" : "auto"; s.setAttribute("aria-hidden", d !== 0); });
  $$("button", dots).forEach((b, i) => b.setAttribute("aria-current", i === cur)); $("#cfcap").textContent = titles[cur]; $("#cflink").href = sls[cur].dataset.href; }
const go = i => { cur = (i + sls.length) % sls.length; cf(); };
$("#prev").onclick = () => go(cur - 1); $("#next").onclick = () => go(cur + 1);
$$("button", dots).forEach((b, i) => b.onclick = () => go(i)); sls.forEach((s, i) => s.onclick = () => go(i));
const cfEl = $(".cf"); cfEl.tabIndex = 0; cfEl.addEventListener("keydown", e => { if (e.key === "ArrowRight") go(cur + 1); if (e.key === "ArrowLeft") go(cur - 1); });
let x0 = null; cfEl.addEventListener("pointerdown", e => x0 = e.clientX);
cfEl.addEventListener("pointerup", e => { if (x0 !== null && Math.abs(e.clientX - x0) > 40) go(cur + (e.clientX < x0 ? 1 : -1)); x0 = null; }); cf();

/* How-it-works wheel: click a step; auto-advances unless reduced motion */
const steps = [["Call or book online", "Reach us 24/7 by phone, or book a visit online."], ["Honest diagnosis", "We explain what's wrong and quote upfront."],
  ["Repair, replace or finance", "You choose. CoolNow™ financing is available."], ["Keep it running", "Tune-ups and the Cool Club maintenance plan."]];
const nodes = $$(".wheel>button"); let wi = 0, timer;
const setW = i => { wi = i; nodes.forEach((b, k) => { const a = ((k - i) * 90 - 90) * Math.PI / 180; b.style.left = 50 + 50 * Math.cos(a) + "%"; b.style.top = 50 + 50 * Math.sin(a) + "%";
  b.setAttribute("aria-pressed", k === i); b.setAttribute("aria-label", `Step ${k + 1}: ${steps[k][0]}`); }); $("#wt").textContent = steps[i][0]; $("#wd").textContent = steps[i][1]; };
nodes.forEach((b, i) => b.addEventListener("click", () => { clearInterval(timer); setW(i); })); setW(0);
if (!RM) timer = setInterval(() => setW((wi + 1) % 4), 5000);

/* Reviews slider with numbered pager */
const rs = $$(".rv figure"), rp = $("#rp"); let ri = 0;
rp.innerHTML = rs.map((_, k) => `<button aria-label="Review ${k + 1}">${k + 1}</button>`).join("");
const showR = i => { ri = (i + rs.length) % rs.length; rs.forEach((f, k) => f.hidden = k !== ri); $$("button", rp).forEach((b, k) => b.setAttribute("aria-current", k === ri)); };
$$("button", rp).forEach((b, k) => b.onclick = () => showR(k)); $("#rprev").onclick = () => showR(ri - 1); $("#rnext").onclick = () => showR(ri + 1); showR(0);
