# 🧠 Brain Tumor Detection using Machine Learning (SVM)

This project presents a Support Vector Machine (SVM)-based solution for detecting brain tumors from MRI scans. The model is built using classical image processing techniques and achieves a high accuracy of **95.12%**, making it a reliable and cost-effective tool for early diagnosis of brain tumors. Designed for medical professionals, it offers an easy-to-use interface with strong backend accuracy.

---

## 🔍 Key Features

- **Dataset**: Curated MRI images from Kaggle, labeled as `TUMOR` and `NO_TUMOR`.
- **Preprocessing**:
  - Resizing images to 200x200 resolution
  - Converting images to grayscale
  - Pixel value normalization for consistency
- **Model**: SVM (Support Vector Machine) trained on features extracted using PCA (Principal Component Analysis).
- **Performance**: Achieves an impressive **95.12% accuracy**, validated on real-world MRI scan data.
- **Deployment**: Comes with a user-friendly interface aimed at assisting medical professionals in diagnosis.

---

## 🛠 Tech Stack

- **Programming Language**: Python
- **Machine Learning Library**: scikit-learn
- **Image Processing**: OpenCV, scikit-image
- **Development Tools**: Jupyter Notebook, Kaggle
- **Additional Libraries**: NumPy, Pandas, Matplotlib

---

## 📌 Project Highlights

- 🏥 **Medical Impact**: Significantly reduces diagnostic time and error rate for tumor detection.
- 🔄 **Methodology**: Hybrid approach combining classical image preprocessing and machine learning (SVM + PCA).
- 🚀 **Future Scope**:
  - Cloud-based deployment for wider accessibility
  - Mobile application integration
  - Comparison with deep learning models (e.g., CNN)

---

## 📂 Files Overview

- `data/` – Preprocessed MRI image datasets  
- `notebooks/` – Jupyter notebooks for EDA, training, and model evaluation  
- `src/` – Core Python scripts for image preprocessing, SVM training, and inference  
- `report/` – Final project documentation (PDF, PPT)

---

## 🚀 How It Works

1. **Input**: Upload an MRI scan image.
2. **Preprocessing**: Resize the image, convert to grayscale, normalize pixel values.
3. **Feature Extraction**: Apply PCA to reduce dimensionality and noise.
4. **Prediction**: Trained SVM model classifies the image as `TUMOR` or `NO_TUMOR`.
5. **Output**: Displays classification label with model confidence.

---

## 🌟 Why This Project?

- ✅ Offers a **cost-effective**, accurate, and fast diagnostic support system.
- ✅ Especially helpful in areas with limited access to radiologists or advanced diagnostic tools.
- ✅ Open-source project designed for healthcare and academic research communities.

---

## 🤝 Collaboration

Open to healthcare collaborations, medical research teams, and contributors with better datasets or deployment ideas. Feel free to raise issues, suggest features, or create pull requests.

---

## 👨‍💻 Developed by

**Kapil Bisht**  
[GitHub: @Kapilbisht2004](https://github.com/Kapilbisht2004)

---

