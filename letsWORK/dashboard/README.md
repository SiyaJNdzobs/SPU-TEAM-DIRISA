# KZN Ward Voter Turnout Interactive Dashboard

This interactive dashboard serves as the public deployment interface for the **DIRISA SDC Student Datathon (Teams Qualification)** project.

---

## 1. How to Run Locally

1. Open a terminal or PowerShell in the repository root:
   ```bash
   cd "C:\Users\Student\Downloads\Big Data\SPU-TEAM-DIRISA"
   ```

2. Activate your Python environment (e.g. Anaconda):
   ```bash
   conda activate base
   ```

3. Launch the dashboard:
   ```bash
   streamlit run letsWORK/dashboard/app.py
   ```

4. The dashboard will automatically launch in your browser at:
   `http://localhost:8501`

---

## 2. How to Deploy to Streamlit Community Cloud (Public Zero-Setup Link)

1. **Push to GitHub**:
   - Push this repository to your GitHub account (e.g., `https://github.com/SiyaJNdzobs/SPU-TEAM-DIRISA`).

2. **Connect to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
   - Click **New app**.
   - Select your repository: `SiyaJNdzobs/SPU-TEAM-DIRISA`.
   - Set the Branch: `main`.
   - Set the Main file path: `letsWORK/dashboard/app.py`.

3. **Deploy**:
   - Click **Deploy!**
   - Streamlit Cloud will automatically install dependencies from `letsWORK/dashboard/requirements.txt` and generate a live public URL (e.g., `https://kzn-voter-turnout-dirisa.streamlit.app`).

---

## 3. Alternative: Deploy to Hugging Face Spaces

1. Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces).
2. Choose **Streamlit** as the Space SDK.
3. Upload `app.py`, `requirements.txt`, and the processed data files, or link your GitHub repository.
4. Your dashboard will be live at `https://huggingface.co/spaces/<your-username>/kzn-voter-turnout`.
