FROM raspbian/systemd

# Install.
RUN \
  apt update && \
  apt -y upgrade && \
  apt install -y sudo
RUN apt install -y systemctl


# Setting up SYSTEMCTL
RUN mkdir -p /etc/systemd/system/
COPY vrms-pi.service /etc/systemd/system/
RUN systemctl daemon-reload
RUN systemctl enable vrms-pi

RUN useradd -ms /bin/bash pi && echo "pi:pi" | chpasswd && adduser pi sudo
USER pi
WORKDIR /home/pi


# Define default command.
CMD ["bash"]