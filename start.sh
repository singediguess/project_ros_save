sudo iptables -t nat -A POSTROUTING -o enxb827ebe97de9 -j MASQUERADE  
sudo iptables -A FORWARD -i enxb827ebe97de9 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT  
sudo iptables -A FORWARD -i wlan0 -o enxb827ebe97de9 -j ACCEPT 

sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
