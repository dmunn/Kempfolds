# Kempfolds Slack Bot

<!-- PROJECT SHIELDS -->
[![Build Status](https://travis-ci.org/dmunn/Kempfolds.svg?branch=master)](https://travis-ci.org/dmunn/Kempfolds)

Get a random Kemfolds image from [Kempfolds blog](http://kempfolds.blogspot.com/)

## Getting Started

This is still in a PoC stage so at this stage a "Getting Started" section cannot be provided.

### Development

#### Prerequisites
A virtual environment using Python 3.10.0

Example - using `pyenv`:
1. `pyenv virtualenv 3.10.0 kempfolds`
2. `pyenv activate kempfolds `

Install the requirements: `pip install -r requirements.txt`

### App

#### Testing
- Run unittests: `make test`

### Web

#### Locally
- Change directory: `cd app`
- Start the webserver: `flask run`
- Access site using `http://localhost:5000`

#### Containerised
- Build image: `docker build -t kempfolds .`
- Run container: `docker run -p 8080:80 kempfolds`
- Access site using `http://localhost:8080`

## Deployment
See [infra/README.md](./infra/README.md) for more information

## TODO
- Store static assets in S3 when hosting remotely (AWS)
    - Use [Flask-S3](https://flask-s3.readthedocs.io/en/latest/) to support this
    - Once added an additional feature can be enabled, speedier static asset updates as it no longer depends on rebuilding the container. A new action should be added to covering the commands to update them, see [Uploading your Static Assets](https://flask-s3.readthedocs.io/en/latest/#uploading-your-static-assets)
- Fix Kempolds instance initialisation - currently too many bootstrapping events to create a usable class object.

## Built With
* Python
* Atoma
* Flask

## Contributing
Please contribute once this is out of a PoC state. Development is based around [trunk-based](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development) so if you spot an issue that can be resolved then please go ahead.

## Versioning

I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/dmunn/Kempfolds/tags).

## License

This project is licensed under the Creative Commons Attribution-Noncommercial-Share Alike 2.0 UK: England & Wales License License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* A huge thank you to the author of the [Kempfolds blog](http://kempfolds.blogspot.com/) and for the efforts of everyone who took the time to post to it.
