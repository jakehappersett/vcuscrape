import splinter

br = Browser()


br.visit('https://ssb.vcu.edu/proddad/bwskfreg.P_AltPin')
br.fill('sid', 'happersettjw')
br.fill('PIN', 'Happ876J')
br.find_by_name(
