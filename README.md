# Emotion-classification-Using EEG Data

## AMIGOS DATASET (A dataset for affect, personality and mood research on individuals and groups)

## GETTING STARTED:-

It is difficult to look at the EEG signal and identify the state of Human mind. In this problem statement a classifier needs to be trained with AMIGOS dataset to predict the state of mind. The state of mind is predicted in terms of valence, arousal, dominance and liking which can further be used to predict the state of mind in terms of expression.

<br>
<center>
<img src ="Assets/down_final.png"  width=800 height=400>  
</center>
<br>

## PROCEDURE:-

The Preprocessed Data is used for training the classifier.
Steps involve in training the dataset:-

1. Extracting the dataset
2. Finding the features
3. Reducing the dimension
4. Training the vector.
5. Checking the Classifier efficiency.

## DATASET DESCRIPTION:-

The AMIGOS dataset consists of the participants' profiles (anonymized participants' data, personality profiles and mood (PANAS) profiles), participant ratings, external annotations, neuro-physiological recordings (EEG, ECG and GSR signals), and video recording (frontal HD, full-body and depth videos) of two experiments:

1. Short videos experiment: In this experiment, 40 volunteers watched a set of 16 short affective video extracts from movies. Each participant was in individual settings and rated each video in valence, arousal, dominance, familiarity and liking, and selected basic emotions (Neutral, Happiness, Sadness, Surprise, Fear, Anger, and Disgust) that they felt during the videos.

2. Long videos experiment: In this experiment, 37 of the participants of the previous experiment watched a set of 4 long affective video extracts from movies. 17 of the participants performed the experiment in individual setting while the other 20 participants did it in group setting, in 5 groups of 4 people. Each participant rated each video in valence, arousal, dominance, familiarity and liking, and selected basic emotions (Neutral, Happiness, Sadness, Surprise, Fear, Anger, and Disgust) that they felt during the videos.

## FINDING THE FEATURES:-

Wavelet transform and Fast Fourier Transform is used to decompose the each channel data into the five features i.e :-

- **Delta (< 4 Hz)**
- **Theta (5-7 Hz)**
- **Alpha (8-15 Hz)**
- **Beta (16-31 Hz)**
- **Gamma (> 32 Hz)**

Energy and Entropy is computed for each feature band from each channel

- **For wavelet features `Total Wavelet Entropy` is calculated**
- **For fourier features `Spectral Entropy` is calculated**

**Short-Time Fourier Transform (STFT)**

- Short-time Fourier transform (STFT) is a sequence of Fourier transforms of a windowed signal.

## Results

### Results on Arousal,Valence,Dominance And Liking:-

|       **Preprocessing Technique**        | **Methods** | **Metrics** | **Arousal** | **Valence** | **Dominance** | **Liking** |
| :--------------------------------------: | :---------: | :---------: | :---------: | :---------: | :-----------: | :--------: |
|                                          |             |             |             |             |               |            |
|                                          |             |             |             |             |               |            |
|                                                          | 40 USERS||||                                                       |
|                                          |             |             |             |             |               |            |
|                                          |             |             |             |             |               |            |
|     `Wavelet(Total Wavelet Entropy)`     |             |             |             |             |               |            |
|                                          |    `ANN`    | `Accuracy`  |   `73.5`    |   `64.7`    |    `60.08`    |   `76.3`   |
|                                          |             |             |             |             |               |            |
|                                          |    `SVC`    | `Accuracy`  |    `75`     |    `61`     |    `61.6`     |  `78.89`   |
|                                          |             |             |             |             |               |            |
|                                          |             | `K-Fold CV` |   `74.6`    |   `63.05`   |    `60.88`    |   `77.6`   |
|                                          |             |             |             |             |               |            |
|                                          |             |   `LOOCV`   |   `75.7`    |   `65.2`    |    `61.6`     |   `76.8`   |
|                                          |             |             |             |             |               |            |
|       `Fourier(Spectral Entropy)`        |             |             |             |             |               |            |
|                                          |    `ANN`    | `Accuracy`  |   `70.5`    |   `63.8`    |    `56.8`     |  `71.03`   |
|                                          |             |             |             |             |               |            |
|                                          |    `SVC`    | `Accuracy`  |    `72`     |   `63.2`    |    `64.8`     |   `69.4`   |
|                                          |             |             |             |             |               |            |
|                                          |             | `K-Fold CV` |   `74.8`    |   `60.7`    |    `63.2`     |   `71.3`   |
|                                          |             |             |             |             |               |            |
|                                          |             |   `LOOCV`   |   `76.6`    |   `61.8`    |    `61.3`     |   `72.1`   |
|                                          |             |             |             |             |               |            |
| `Fusion of Wavelet and Fourier with PCA` |             |             |             |             |               |            |
|                                          |    `SVC`    | `Accuracy`  |   `79.3`    |   `64.08`   |    `62.5`     |   `76.2`   |
|                                          |             |             |             |             |               |            |
|                                          |             | `K-Fold CV` |   `77.1`    |   `64.04`   |    `61.3`     |   `76.3`   |
|                                          |             |             |             |             |               |            |
|                                          |             |   `LOOCV`   |   `76.8`    |   `63.1`    |     `61`      |   `76.8`   |
|                                          |             |             |             |             |               |            |
|                                          |    `RVC`    | `Accuracy`  |   `77.4`    |   `61.3`    |     `59`      |    `78`    |
|                                          |             |             |             |             |               |            |
|                                          |             |             |             |             |               |            |
|                                                          | 20 USERS||||                                                      
|                                          |             |             |             |             |               |            |
|                                          |             |             |             |             |               |            |
|     `Wavelet(Relative Energy)`           |             |             |             |             |               |            |
|                                          |    `RVC`    | `Accuracy`  |   `73.07`   |   `64.51`   |    `59.54`    |   `73.86`  |
|                                          |             |             |             |             |               |            |
|                                          |    `SVC`    | `Accuracy`  |    `76.92`  |    `73.11`  |    `67.17`    |  `80.11`   |
|                                          |             |             |             |             |               |            |
|                                          |`Stacking Classifier`      | `Accuracy`  |   `75.96`   |   `76.34`     |    `70.22` |   `80.11`  |
|                                          |             |             |             |             |               |            |
|       `Fourier(Spectral Power)`          |             |             |             |             |               |            |
|                                          |    `RVC`    | `Accuracy`  |   `73.07`   |   `63.44`   |    `63.35`    |   `77.27`  |
|                                          |             |             |             |             |               |            |
|                                          |    `SVC`    | `Accuracy`  |    `80.76`  |    `68.81`  |    `63.35`    |  `77.27`   |
|                                          |             |             |             |             |               |            |
|                                          |`Stacking Classifier`      | `Accuracy`  |   `71.15`   |   `60.21`     |    `72.51` |   `78.97`  |
|                                          |             |             |             |             |               |            |
|       `Feature_Fusion(Wavelet Energy + Spectral Power)`|             |             |             |               |            |            |
|                                          |    `RVC`    | `Accuracy`  |   `75.00`   |   `63.44`   |    `66.41`    |   `75.00`  |
|                                          |             |             |             |             |               |            |
|                                          |    `SVC`    | `Accuracy`  |    `77.88`  |    `67.74`  |    `74.04`    |  `80.68`   |
|                                          |             |             |             |             |               |            |
|                                          |`Stacking Classifier`      | `Accuracy`  |   `80.77`   |   `69.89`     |    `71.75` |   `78.40`  |
|                                          |             |             |             |             |               |            |
|        `Wavelet Transformation [Non-Overlapping]`      |             |             |             |               |            |            |
|                                          |  `ANN`      | `Accuracy`  |   `81.80`   |   `75.65`   |    `78.97`    |  `83.95`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 1D`   | `Accuracy`  |   `78.64`   |   `69.55`   |    `73.13`    |  `81.11`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 2D`   | `Accuracy`  |   `80.22`   |   `75.50`   |    `76.67`    |  `82.95`   |
|                                          |             |             |             |             |               |            |
|       `Wavelet Transformation [Overlapping]`           |             |             |             |               |            |            |
|                                          |  `ANN`      | `Accuracy`  |   `93.28`   |   `91.05`   |    `91.59`    |  `93.36`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 1D`   | `Accuracy`  |   `89.9`    |   `85.95`   |    `88.21`    |  `90.89`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 2D`   | `Accuracy`  |   `92.3`    |   `90.35`   |    `91.51`    |  `93.45`   |
|                                          |             |             |             |             |               |            |
| `Short Time Fast Fourier Transformation [Non-Overlapping]` |         |             |             |               |            |            |
|                                          |  `ANN`      | `Accuracy`  |   `65.00`   |   `55.60`   |    `60.32`    |  `79.95`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 1D`   | `Accuracy`  |   `71.33`   |   `66.56`   |    `65.66`    |  `80.18`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 2D`   | `Accuracy`  |   `75.41`   |   `71.81`   |    `71.37`    |  `82.28`   |
|                                          |             |             |             |             |               |            |
| `Short Time Fast Fourier Transformation [Overlapping]` |             |             |             |               |            |            |
|                                          |  `ANN`      | `Accuracy`  |   `88.80`   |   `89.05`   |    `90.59`    |  `91.07`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 1D`   | `Accuracy`  |   `91.45`   |   `92.93`   |    `93.47`    |  `93.76`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 2D`   | `Accuracy`  |   `94.22`   |   `93.78`   |    `94.04`    |  `94.44`   |
|                                          |             |             |             |             |               |            |
| `Feature Fusion [Non-Overlapping]`       |             |             |             |             |               |            |
|                                          |  `ANN`      | `Accuracy`  |   `84.41`   |   `78.76`   |    `81.09`    |  `85.45`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 1D`   | `Accuracy`  |   `78.30`   |   `69.67`   |    `70.09`    |  `80.65`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 2D`   | `Accuracy`  |   `81.79`   |   `75.59`   |    `78.67`    |  `84.13`   |
|                                          |             |             |             |             |               |            |
| `Feature Fusion [Overlapping]`           |             |             |             |             |               |            |
|                                          |  `ANN`      | `Accuracy`  |   `95.38`   |   `95.69`   |    `96.15`    |  `96.76`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 1D`   | `Accuracy`  |   `93.66`   |   `93.14`   |    `92.62`    |  `92.46`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 2D`   | `Accuracy`  |   `96.63`   |   `95.87`   |    `96.30`    |  `96.77`   |

## Usage

- `DataConversion`: Code to convert the amigos dataset from `matlab files` into `csv files`
- `Dataset`: `Transformed data` to all users in `pickle` format
- `Fourier`: Code for `fourier transformation`
- `Wavelet`: Code for `wavelet transformation`
- `Src`: Code to apply the wavelet and fourier transformation on raw data and store the data into dataset
- `Models`: Code for different `Machine Learning` and `Deep Learning` `methods` applied

## Contributers

<table>
  <tr>
    <td align="center"><a href="https://github.com/soumyajit4419"><img src="https://avatars2.githubusercontent.com/u/46092576?s=460&u=32c24b6d0308f5fdfff2ab740a9f525894edb582&v=4" width="100px;" alt=""/><br /><sub><b>Soumyajit Behera</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Rahul1582"><img src="https://avatars2.githubusercontent.com/u/47784845?s=400&u=1e9898b8c4b762fcda1f37864c16b5de11f885ce&v=4" width="100px;" alt=""/><br /><sub><b>Rahul Kumar Patro</b></sub></a><br /></td>
  </tr>
</table>
