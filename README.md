# Emotion-classification-Using EEG Data

## AMIGOS DATASET (A dataset for affect, personality and mood research on individuals and groups)

## PROBLEM STATEMENT:-

It is difficult to look at the EEG signal and identify the state of Human mind. In this problem statement a classifier needs to be trained with AMIGOS dataset to predict the state of mind. The state of mind is predicted in terms of valence, arousal. which can further be used to predict the state of mind in terms of expression.

<br>
<center>
<img src ="Assets/image.gif"  width=600 height=400>  
</center>
<br>

## PROCEDURE TO SOLVE THE PROBLEM:-

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

## Usage

- `DataConversion`: Code to convert the amigos dataset from `matlab files` into `csv files`
- `Dataset`: `Transformed data` to all users in `pickle` format
- `Fourier`: Code for `fourier transformation`
- `Wavelet`: Code for `wavelet transformation`
- `Src`: Code to apply the wavelet and fourier transformation on raw data and store the data into dataset
- `Models`: Code for different `Machine Learning` and `Deep Learning` `methods` applied

## Results

### Results on Arousal,Valence,Dominance And Liking:-

|       **Preprocessing Technique**        | **Methods** | **Metrics** | **Arousal** | **Valence** | **Dominance** | **Liking** |
| :--------------------------------------: | :---------: | :---------: | :---------: | :---------: | :-----------: | :--------: |
|     `Wavelet(Total Wavelet Entropy)`     |             |             |             |             |               |            |
|                                          |    `ANN`    | `Accuracy`  |   `73.5`    |   `64.7`    |   `60.08`     |  `76.3`    |
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
| `Short Time Fast Fourier Transformation` |             |             |             |             |               |            |
|                                          |  `CNN 1D`   | `Accuracy`  |   `95.45`   |   `94.59`   |    `94.41`    |  `94.88`   |
|                                          |             |             |             |             |               |            |
|                                          |  `CNN 2D`   | `Accuracy`  |   `97.72`   |   `96.38`   |    `96.65`    |  `97.51`   |

## Contributers

<table>
  <tr>
    <td align="center"><a href="https://github.com/soumyajit4419"><img src="https://avatars2.githubusercontent.com/u/46092576?s=460&u=32c24b6d0308f5fdfff2ab740a9f525894edb582&v=4" width="100px;" alt=""/><br /><sub><b>Soumyajit Behera</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Rahul1582"><img src="https://avatars2.githubusercontent.com/u/47784845?s=400&u=1e9898b8c4b762fcda1f37864c16b5de11f885ce&v=4" width="100px;" alt=""/><br /><sub><b>Rahul Kumar Patro</b></sub></a><br /></td>
  </tr>
</table>
