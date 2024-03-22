# YoutubeStreamAnalytics

Welcome to the YoutubeStreamAnalytics repository! This project dives into the fascinating world of real-time data analytics with a specific focus on YouTube video performance metrics. Leveraging the YouTube API, Apache Kafka, and other cutting-edge data engineering technologies, YoutubeStreamAnalytics offers insights into video likes, views, comments, and more, all in real-time.

## Project Overview

YoutubeStreamAnalytics is an advanced data pipeline that extracts YouTube video data, processes it through Apache Kafka, and analyzes it to unearth valuable insights about video performance. It stands as a beacon for aspiring data engineers and analysts, providing a real-world application of data engineering principles in the context of popular social media metrics.

## Features

- **Real-time Data Extraction**: Uses the YouTube Data API to fetch current video data.
- **Streaming Data Processing**: Employs Apache Kafka for robust management of the streaming data pipeline.
- **In-depth Analytics**: Performs comprehensive analysis on video performance metrics.
- **Scalability**: Designed to efficiently scale up for handling large volumes of data.
- **Educational Value**: Offers a practical learning experience for data engineering enthusiasts.

## Getting Started

### Prerequisites

- Python 3.10(minimum)
- Apache Kafka
- GCP Youtube API key
- Telegram API
- Docker
- Confluent Containers (Zookeeper, Kafka, Schema Registry, Connect, ksqlDB, Control Center)

### Setup and Installation

1. Clone this repository:

```sh
git clone https://github.com/hizkiarenvil/YoutubeStreamAnalytics.git
```
Navigate to the project directory:
```sh
cd YoutubeStreamAnalytics
```
Install the required Python packages:
```sh
pip install -r requirements.txt
```
Configure your environment by updating the config/config.local file with your GCP YouTube API key and other necessary settings.

Start the Confluent Platform using Docker Compose:
```sh
docker-compose up -d
```
Run the main script to start the data processing pipeline:
```sh
python YoutubeAnalytics.py
```
## How to Contribute
Contributions to YoutubeStreamAnalytics are welcome! Whether it's bug fixes, new features, or improvements to the documentation, your help is appreciated. Please feel free to fork the repository and submit pull requests.

## Acknowledgments
Special thanks to the Apache Kafka project for the streaming platform.
Gratitude to the YouTube Data API for providing access to video metrics.
Inspired by the YoutubeAnalytics project by Yusuf Ganiyu (https://www.youtube.com/watch?v=0aqSjJ3-4NI&list=PL_Ct8Cox2p8VUtmhZYNpGE_yFORZDi_nY) , which provided valuable insights and inspiration for this project.
