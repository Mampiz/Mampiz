<h1 align="center">Josep Mampel Marqués</h1>

<p align="center">
  Software engineer in Barcelona — embedded automotive code by day,<br>
  Kubernetes controllers by night. Confusing elevator pitch, fun life.
</p>

<p align="center">
  <sub><b>Go</b> · <b>Kubernetes</b> · Platform engineering · Automotive firmware</sub>
</p>
<br>
## About

I got into this because I liked taking things apart to see why they broke. That instinct got me into automotive: bootloaders, AUTOSAR, diagnostics, secure boot — a world where you can't just redeploy on Friday afternoon, because your code is now inside somebody's car doing 120 on the AP-7.

Somewhere along the way I discovered platform engineering and realised the cloud people had reinvented everything I already knew, but with better tooling and much nicer error messages. Signed firmware? Signed container images. A bootloader refusing to run unverified code? Admission webhook. Watchdog timer? Liveness probe. So now I do both, and I'm slowly leaning cloud-ward.

Outside of that: I'm from here, I speak Spanish and Catalan, and I will absolutely talk your ear off about why `latest` is a terrible image tag if you let me.

<br>

## Toolbox

<table>
  <tr>
    <td width="190"><b>Every day, happily</b></td>
    <td><a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=go,kubernetes,docker,linux,git,bash&theme=dark" alt="Go, Kubernetes, Docker, Linux, Git, Bash"/></a></td>
  </tr>
  <tr>
    <td><b>At work, in automotive</b></td>
    <td><a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=c,cpp,python&theme=dark" alt="C, C++, Python"/></a></td>
  </tr>
  <tr>
    <td><b>Also comfortable with</b></td>
    <td><a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=ts,react,postgres,redis,kafka,fastapi,nginx,aws,prometheus,grafana,githubactions&theme=dark" alt="TypeScript, React, Postgres, Redis, Kafka, FastAPI, Nginx, AWS, Prometheus, Grafana, GitHub Actions"/></a></td>
  </tr>
  <tr>
    <td><b>Currently learning</b></td>
    <td><a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=terraform&theme=dark" alt="Terraform"/></a></td>
  </tr>
</table>

<br>

## What I've been building

<table>
  <tr>
    <td width="50%" valign="top">

### [webapp-operator](https://github.com/Mampiz/webapp-operator)

`Go` · `controller-runtime` · `Kubernetes`

A Kubernetes operator. You write one small `WebApp` resource and it takes care of the Deployment, the Service, the autoscaler and the disruption budget — forever.

Admission webhooks, Prometheus metrics, a Grafana dashboard, and scale numbers I actually measured instead of vibing.

  </td>
    <td width="50%" valign="top">

### [idp-backstage](https://github.com/Mampiz/idp-backstage)

`Backstage` · `Argo CD` · `GitHub Actions`

An Internal Developer Platform. Fill in a form and, before you finish reading the confirmation page, you have a GitHub repo with CI *and* a live workload in Kubernetes.

My favourite part isn't the demo — it's the README section on what happens when it half-fails. Turns out that's the interesting engineering.

  </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">

### [llm-gateway](https://github.com/Mampiz/llm-gateway) &nbsp;<sub><i>work in progress, don't judge</i></sub>

`Go` · `concurrency` · `Redis`

A proxy in front of multiple model providers: one API, streaming, distributed rate limiting, failover and caching. Mostly an excuse to write concurrent Go that's harder than a worker-pool tutorial.

  </td>
  </tr>
</table>

---

<p align="center">
  <a href="https://linkedin.com/in/josep-mampel-marques"><img src="https://skillicons.dev/icons?i=linkedin&theme=dark" alt="LinkedIn"/></a>
  &nbsp;
  <a href="mailto:josepmampel20@gmail.com"><img src="https://skillicons.dev/icons?i=gmail&theme=dark" alt="Email"/></a>
  &nbsp;
  <a href="https://github.com/Mampiz"><img src="https://skillicons.dev/icons?i=github&theme=dark" alt="GitHub"/></a>
</p>

<p align="center">
  <sub>Barcelona · open to remote 
</p>
