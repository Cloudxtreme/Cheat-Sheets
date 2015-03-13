sudo apt-get install -y mongodb
sudo service mongodb start

# For remote connections add folling line to "/etc/mongodb.conf"
bind_ip = 0.0.0.0

# Web mongo GUI with Ruby gem
gem install bson_ext
gem install bson_ext -v 1.9.2
gem install genghisapp
genghisapp # http://localhost:5678/
genghisapp --kill
