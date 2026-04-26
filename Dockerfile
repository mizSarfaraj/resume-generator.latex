FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-latex-extra \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Updated CMD to point to template/resume.tex and delete *.tex at the end
CMD ["/bin/sh", "-c", "python3 script/build.py $PROFILE && pdflatex template/resume.tex && rm -f *.aux *.log *.out *.tex"]