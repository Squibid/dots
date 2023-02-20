THEMEDIR = /usr/share/grub/themes/custom

install:
	mkdir -p $(THEMEDIR)
	cp theme.txt background.png $(THEMEDIR)
	sed -i '/GRUB_THEME=/d' /etc/default/grub
	printf "GRUB_THEME=$(THEMEDIR)/theme.txt" >> /etc/default/grub
	update-grub

uninstall:
	rm $(THEMEDIR)/theme.txt $(THEMEDIR)/background.png
	sed -i '/GRUB_THEME=/d' /etc/default/grub
	update-grub
