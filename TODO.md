## Phase 1: Software & Testing (Code Refactoring & Test Automation)
- [ ] **Task 1.1: Automate GDS & Image Extraction**
  - [ ] Add `c.write_gds("build/graphene_photodetector.gds")`
  - [ ] Add logic to save `build/graphene_photodetector.png` using `c.plot()` and `matplotlib`
- [ ] **Task 1.2: Write Unit Tests**
  - [ ] Set up `pytest` environment
  - [ ] Create `test_layout.py` file
  - [ ] Write test case: Verify `.gds` and `.png` files are successfully generated in the `build/` folder after running the Python script
  - [ ] Write test case: Verify the generated files are not 0 bytes in size

## Phase 2: Containerization (Unified Execution Environment)
- [ ] **Task 2.1: Write Dockerfile**
  - [ ] Set Base Image (e.g., `python:3.10-slim` or `ubuntu:22.04`)
  - [ ] Install essential system packages (e.g., `klayout`, other dependencies)
  - [ ] Install Python dependencies (`gdsfactory`, `pytest`, `matplotlib`, etc.)
  - [ ] Copy layout scripts and test files (`COPY`)
- [ ] **Task 2.2: Local or Raspberry Pi Build Testing**
  - [ ] Run `docker build -t layout-pipeline .` on the local laptop and verify success
  - [ ] Verify build success on the Raspberry Pi
  - [ ] Confirm the layout script and `pytest` run correctly inside the container

## Phase 3: Automation Infrastructure (Raspberry Pi CI/CD Integration)
- [ ] **Task 3.1: Set Up GitHub Self-Hosted Runner**
  - [ ] Navigate to GitHub Repository > Settings > Actions > Runners
  - [ ] Create "New self-hosted runner" (OS: Linux, Architecture: ARM64)
  - [ ] Execute the provided installation script in the Raspberry Pi terminal
  - [ ] Register `run.sh` as a background service (`systemd`) to keep it listening continuously
- [ ] **Task 3.2: Write GitHub Actions Workflow (`.yml`)**
  - [ ] Create `.github/workflows/layout_pipeline.yml` file
  - [ ] Specify the `runs-on: self-hosted` tag
  - [ ] Step 1: Checkout repository code (`actions/checkout@v4`)
  - [ ] Step 2: Execute `test_layout.py` within the Docker environment
  - [ ] Step 3: If successful, upload the files in the `build/` directory to GitHub Artifacts (`actions/upload-artifact@v4`)

## Phase 4: Demo Preparation (Interview Scenario Planning)
- [ ] **Task 4.1: Prepare Failure Scenario**
  - [ ] Intentionally push code with an error (e.g., negative value for electrode length)
  - [ ] Verify that the Raspberry Pi runner catches the error via `pytest` and the pipeline fails (Red)
- [ ] **Task 4.2: Prepare Success Scenario**
  - [ ] Fix the code and push the correct version
  - [ ] Verify that the pipeline passes (Green) and the `.gds` and `.png` files are uploaded to the Artifacts tab
  - [ ] Review the demo flow so it can be smoothly downloaded and presented to the interviewers