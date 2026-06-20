<!-- root@federico:~$ cat /etc/motto
I build systems — and break them.
-->

<div align="center">
  <img alt="Terminal" src="./output.gif" width="98%" />
</div>

<div align="center">
  <h1>Federico López</h1>
  <p><code>I build systems — and break them.</code></p>
  <p>
    <img src="https://img.shields.io/badge/Full_Stack_Engineer-0d1117?style=flat-square&logo=python&logoColor=10B981&labelColor=0d1117&color=10B981" alt="Full Stack Engineer" />
    <img src="https://img.shields.io/badge/Offensive_Security_(AI)-0d1117?style=flat-square&logo=hackthebox&logoColor=ef4444&labelColor=0d1117&color=ef4444" alt="Offensive Security (AI)" />
    <img src="https://img.shields.io/badge/Founder-0d1117?style=flat-square&logo=rocket&logoColor=10B981&labelColor=0d1117&color=10B981" alt="Founder" />
    <img src="https://img.shields.io/badge/Montevideo_%F0%9F%87%BA%F0%9F%87%BE-0d1117?style=flat-square&logoColor=10B981&labelColor=0d1117&color=30363d" alt="Montevideo, Uruguay" />
  </p>
</div>

```bash
$ whoami
federico — ingeniero full stack y operador ofensivo. Construyo sistemas que
mueven dinero y datos a escala, y rompo los que no deberían dejarme entrar.
```

## `~/build`

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://autop2p.dev">AutoP2P</a></h3>
      <p>SaaS multi-tenant para automatizar anuncios P2P (C2C) de Binance: motor de repricing, gestión multi-anuncio y dashboard en tiempo real. Aislamiento por tenant con RLS en Postgres.</p>
      <p>
        <img src="https://img.shields.io/badge/Binance_P2P_%C2%B7_multi--tenant_SaaS-0d1117?style=flat-square&labelColor=0d1117&color=10B981" alt="Binance P2P, multi-tenant SaaS" />
        <img src="https://img.shields.io/badge/2.2k%2B_tests_%C2%B7_71_ADRs_%C2%B7_hexagonal-0d1117?style=flat-square&labelColor=0d1117&color=10B981" alt="2.2k+ tests, 71 ADRs, hexagonal" />
        <br/>
        <img src="https://img.shields.io/badge/FastAPI_%C2%B7_PostgreSQL_%C2%B7_Redis_Streams-0d1117?style=flat-square&logo=fastapi&logoColor=10B981&labelColor=0d1117&color=30363d" alt="Stack: FastAPI, PostgreSQL, Redis Streams" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://labs.pentagoo.uy">Pentagoo Labs</a></h3>
      <p>Software factory: scrapers industriales, automatización, integraciones (pagos/CRM/ERP), pipelines de datos y dashboards. Del MVP a producción en días, no meses.</p>
      <p>
        <img src="https://img.shields.io/badge/scraping_%C2%B7_automation_%C2%B7_data_pipelines-0d1117?style=flat-square&labelColor=0d1117&color=10B981" alt="Scraping, automation, data pipelines" />
        <img src="https://img.shields.io/badge/MVP_en_d%C3%ADas%2C_no_meses-0d1117?style=flat-square&labelColor=0d1117&color=10B981" alt="MVP en días, no meses" />
        <br/>
        <img src="https://img.shields.io/badge/Python_%C2%B7_Playwright_%C2%B7_Docker-0d1117?style=flat-square&logo=python&logoColor=10B981&labelColor=0d1117&color=30363d" alt="Stack: Python, Playwright, Docker" />
      </p>
    </td>
  </tr>
</table>

## `~/break`

<table>
  <tr>
    <td valign="top">
      <h3><a href="https://rekon.sh">Rekon</a> &nbsp;<img src="https://img.shields.io/badge/offensive_security-AI--powered-0d1117?style=flat-square&logo=hackthebox&logoColor=ef4444&labelColor=0d1117&color=ef4444" alt="AI-powered offensive security" /></h3>
      <p><em>Lo que tu scanner no ve, nosotros lo explotamos.</em> Pentesting potenciado por IA con motor propio: 291 módulos en paralelo y un pipeline <code>ROE → Recon → Scan → Exploit → Validate → Report</code> (Operator Gate entre Scan y Exploit) con evidencia encadenada por SHA-256. <strong>Operator Gate</strong>: un pentester humano aprueba cada exploit antes de ejecutarlo — la IA propone, el operador autoriza. No es auto-pwn.</p>
      <p>
        <img src="https://img.shields.io/badge/291_m%C3%B3dulos_IA_%C2%B7_Operator_Gate-0d1117?style=flat-square&labelColor=0d1117&color=ef4444" alt="291 módulos IA, Operator Gate" />
        <img src="https://img.shields.io/badge/ROE--gated_%C2%B7_fail--closed_%C2%B7_evidencia_SHA--256-0d1117?style=flat-square&labelColor=0d1117&color=ef4444" alt="ROE-gated, fail-closed, evidencia SHA-256" />
        <br/>
        <img src="https://img.shields.io/badge/Pentest_%C2%B7_Red_Team_%C2%B7_IR_%C2%B7_Smart_Contracts_%C2%B7_LLM%2FAI-0d1117?style=flat-square&labelColor=0d1117&color=30363d" alt="Pentest, Red Team, IR, Smart Contracts, LLM/AI" />
      </p>
    </td>
  </tr>
</table>

## `~/research`

<p>Disclosure responsable y auditoría de código a gran escala — investigación pública, verificable, sin NDA:</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/WebKit_%2F_Safari-0d1117?style=flat-square&logo=safari&logoColor=ef4444&labelColor=0d1117&color=ef4444" alt="WebKit / Safari" />
      <p>Auditoría de <strong>17.773 archivos</strong> del motor → <strong>3 bugs confirmados</strong>.</p>
    </td>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/WordPress_6.7_AI_Client-0d1117?style=flat-square&logo=wordpress&logoColor=ef4444&labelColor=0d1117&color=ef4444" alt="WordPress 6.7 AI Client" />
      <p><strong>Prompt injection</strong> → ejecución de PHP en el plugin de IA.</p>
    </td>
  </tr>
</table>

## `~/lab`

<p>Donde experimento sin miedo (snapshots + rollback). Self-hosting serio y modelos locales:</p>

<div align="center">
  <img src="https://img.shields.io/badge/homelab-Proxmox_%C2%B7_Coolify_%C2%B7_Gitea_%C2%B7_Grafana%2FPrometheus-0d1117?style=flat-square&logo=proxmox&logoColor=10B981&labelColor=0d1117&color=30363d" alt="Homelab: Proxmox, Coolify, Gitea, Grafana/Prometheus" />
  <img src="https://img.shields.io/badge/LLMs_locales-Ollama_%C2%B7_qwen3_%C2%B7_deepseek--r1_%C2%B7_Foundation--Sec--8B-0d1117?style=flat-square&logo=ollama&logoColor=10B981&labelColor=0d1117&color=30363d" alt="LLMs locales: Ollama, qwen3, deepseek-r1, Foundation-Sec-8B" />
</div>

## `~/stack`

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,ts,fastapi,react,nextjs,tailwind,nodejs&theme=dark" alt="Python, TypeScript, FastAPI, React, Next.js, Tailwind, Node.js" />
  <br/>
  <img src="https://skillicons.dev/icons?i=postgres,redis,docker,linux,bash,git,cloudflare&theme=dark" alt="PostgreSQL, Redis, Docker, Linux, Bash, Git, Cloudflare" />
</div>

## `~/metrics`

<div align="center">
  <img width="60%" src="https://streak-stats.demolab.com?user=federicolopeza&theme=transparent&ring=10B981&fire=ef4444&currStreakLabel=10B981&border=30363d" alt="GitHub Streak" />
</div>

<div align="center">
  <img width="98%" src="https://github-readme-activity-graph.vercel.app/graph?username=federicolopeza&bg_color=0d1117&color=c9d1d9&line=10B981&point=10B981&area=true&hide_border=true" alt="Contribution Graph" />
</div>

## `~/contrib`

<div align="center">
  <img src="./breakout/custom.svg" alt="Breakout Contribution Game" width="98%" />
</div>

## `~/writing`

<div align="center">
  <a href="https://federicolopez.uy/blog"><img src="https://img.shields.io/badge/Notas_desde_la_trinchera-deep--dives_t%C3%A9cnicos-0d1117?style=for-the-badge&logo=substack&logoColor=10B981&labelColor=0d1117&color=10B981" alt="Blog — Notas desde la trinchera" /></a>
</div>

## `~/contact`

<div align="center">
  <a href="https://federicolopez.uy"><img src="https://img.shields.io/badge/trabajemos_juntos-federicolopez.uy-0d1117?style=for-the-badge&logo=vercel&logoColor=10B981&labelColor=0d1117&color=10B981" alt="Portfolio — trabajemos juntos" /></a>
  <br/>
  <a href="https://autop2p.dev"><img src="https://img.shields.io/badge/AutoP2P-autop2p.dev-0d1117?style=for-the-badge&logo=binance&logoColor=10B981&labelColor=0d1117&color=10B981" alt="AutoP2P" /></a>
  <a href="https://rekon.sh"><img src="https://img.shields.io/badge/Rekon-rekon.sh-0d1117?style=for-the-badge&logo=hackthebox&logoColor=ef4444&labelColor=0d1117&color=ef4444" alt="Rekon" /></a>
  <a href="https://labs.pentagoo.uy"><img src="https://img.shields.io/badge/Pentagoo_Labs-labs.pentagoo.uy-0d1117?style=for-the-badge&logo=flask&logoColor=10B981&labelColor=0d1117&color=10B981" alt="Pentagoo Labs" /></a>
  <br/>
  <a href="mailto:federico@pentagoo.uy"><img src="https://img.shields.io/badge/email-federico%40pentagoo.uy-0d1117?style=for-the-badge&logo=gmail&logoColor=10B981&labelColor=0d1117&color=30363d" alt="Email" /></a>
  <a href="https://www.linkedin.com/in/federicolopeza"><img src="https://img.shields.io/badge/linkedin-federicolopeza-0d1117?style=for-the-badge&logo=linkedin&logoColor=10B981&labelColor=0d1117&color=30363d" alt="LinkedIn" /></a>
</div>

```bash
$ echo "status=ONLINE | tz=UYT(UTC-3) | building=AutoP2P·Rekon·Pentagoo | open_to=collaborations"
```
