<h1 align="center">Hey, I'm Josep 👋</h1>

<p align="center">
Software engineer in Barcelona. I write embedded automotive code by day and Kubernetes controllers by night, which makes for a confusing elevator pitch but a fun life.
</p>

---

### A bit about me

I got into this because I liked taking things apart to see why they broke. That instinct got me into automotive: bootloaders, AUTOSAR, diagnostics, secure boot — a world where you can't just redeploy on Friday afternoon, because your code is now inside somebody's car doing 120 on the AP-7.

Somewhere along the way I discovered platform engineering and realised the cloud people had reinvented everything I already knew, but with better tooling and much nicer error messages. Signed firmware? That's signed container images. A bootloader refusing to run unverified code? Admission webhook. Watchdog timer? Liveness probe. So now I'm doing both, and slowly leaning cloud-ward.

Outside of that: I'm from here, I speak Spanish and Catalan, and I will absolutely talk your ear off about why `latest` is a terrible image tag if you let me.

---

### 🛠️ Stuff I work with

**Every day, happily**

[![My Skills](https://skillicons.dev/icons?i=go,kubernetes,docker,linux,git,bash&theme=dark)](https://skillicons.dev)

**Professionally, in the automotive world**

[![My Skills](https://skillicons.dev/icons?i=c,cpp,python&theme=dark)](https://skillicons.dev)

**Also comfortable with**

[![My Skills](https://skillicons.dev/icons?i=ts,react,postgres,redis,kafka,fastapi,nginx,aws,prometheus,grafana,githubactions&theme=dark)](https://skillicons.dev)

**Currently learning**

[![My Skills](https://skillicons.dev/icons?i=terraform&theme=dark)](https://skillicons.dev)

---

### 🚧 What I've been building

**[webapp-operator](https://github.com/Mampiz/webapp-operator)** — A Kubernetes operator in Go. You write one small `WebApp` resource, and it takes care of the Deployment, the Service, the autoscaler and the disruption budget, forever. It has admission webhooks, Prometheus metrics, a Grafana dashboard, and scale numbers I actually measured instead of vibing.

**[idp-backstage](https://github.com/Mampiz/idp-backstage)** — An Internal Developer Platform. Fill in a form, and before you finish reading the confirmation page you've got a GitHub repo with CI *and* a live workload in Kubernetes. My favourite part isn't the demo, it's the section of the README about what happens when it half-fails. Turns out that's the interesting engineering.

**LLM gateway** *(in progress, don't judge)* — A Go proxy in front of multiple model providers: one API, streaming, distributed rate limiting, failover, caching. Mostly an excuse to write concurrent Go that's harder than a worker-pool tutorial.

---

### 💭 Opinions I'll defend

- `latest` is a promise you can't keep. My operator rejects it and tells you why.
- If you didn't measure it, don't put a number on it.
- Everyone gets the happy path right. The interesting part is the failure path.
- Docs you didn't write don't exist.

---

### 📫 Say hi

<p align="center">
  <a href="https://linkedin.com/in/josep-mampel-marques"><img src="https://skillicons.dev/icons?i=linkedin&theme=dark" alt="LinkedIn"/></a>
  <a href="mailto:josepmampel20@gmail.com"><img src="https://skillicons.dev/icons?i=gmail&theme=dark" alt="Email"/></a>
  <a href="https://github.com/Mampiz"><img src="https://skillicons.dev/icons?i=github&theme=dark" alt="GitHub"/></a>
</p>

<p align="center">
  <sub>Barcelona 🇪🇸 · open to remote · currently looking for platform / cloud infrastructure roles</sub>
</p>
