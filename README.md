# RosPug CI/CD Proof of Concept

Minimal proof of concept for Slide 8: a `git push` automatically triggers a
Colcon build + test pipeline via GitHub Actions.

## What's inside

```
src/rospug_demo/        # ament_python ROS 2 package
  ├── rospug_demo/talker.py   # minimal node publishing on rospug/status
  ├── test/test_talker.py     # pytest unit tests, picked up by colcon test
  ├── package.xml
  └── setup.py
.github/workflows/ci.yml      # the actual CI/CD pipeline
```

The workflow runs in a `ros:humble-ros-base` container, so the build
environment matches what you'd use for real RosPug packages (ROS 2 Humble).

## One-time setup (do this BEFORE the demo)

```bash
cd rospug-cicd-poc
git init
git add .
git commit -m "Initial RosPug CI/CD proof of concept"
```

Create an empty repo on GitHub (no README/license, so it stays empty), then:

```bash
git remote add origin git@github.com:<your-username>/rospug-cicd-poc.git
git branch -M main
git push -u origin main
```

Pushing already triggers the pipeline once — let it run fully so the Docker
image layer is warm-ish on GitHub's side and you've confirmed everything
passes. Go to the repo's **Actions** tab and confirm you see a green run.

## During the live demo

1. Have the GitHub **Actions** tab open on screen, repo selected.
2. Make a trivial visible change live, e.g. bump the heartbeat message:
   ```bash
   sed -i "s/RosPug heartbeat/RosPug heartbeat - sprint1 demo/" src/rospug_demo/rospug_demo/talker.py
   git add -A
   git commit -m "demo: live CI trigger"
   git push
   ```
3. Switch to the Actions tab — a new run appears within a few seconds.
   Click into it to show the live log: checkout → rosdep → colcon build →
   colcon test, all green.

Expect ~1–3 minutes total (mostly pulling the ROS image), so talk through
the architecture slide while it runs instead of standing in silence.

## Notes / things you might want to extend later (Sprint 2+)

- Add a Docker build+push step for multi-arch (x86 + ARM64) images — this is
  what Slide 9's "Next Steps" references.
- Add an Ansible deploy job gated on the test job succeeding, for the OTA
  push to the actual Go2.
- If you want linting in the pipeline too, add `ament_flake8` and
  `ament_pep257` test files under `test/` — skipped here to keep the demo
  fast and reliable on stage.
