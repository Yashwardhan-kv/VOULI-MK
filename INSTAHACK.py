@@ -1,3 +1,4 @@

'''
TODO LIST:
	Fix and make proxy function better
@@ -88,7 +89,8 @@ def IsUserExists(self):
	def Login(self, password):
		sess = requests.Session()

		sess.proxies = { "http": self.CurrentProxy, "https": self.CurrentProxy }
		if len(self.CurrentProxy) > 0:
			sess.proxies = { "http": self.CurrentProxy, "https": self.CurrentProxy }

		#build requests headers
		sess.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
@@ -119,8 +121,11 @@ def Login(self, password):
		data = json.loads(r.text)
		if (data['status'] == 'fail'):
			print (data['message'])
			print ('[$] Try to use proxy after fail.')
			randomProxy() #Check that, may contain bugs

			UsePorxy = Input('[*] Do you want to use proxy (y/n): ').upper()
			if (UsePorxy == 'Y' or UsePorxy == 'YES'):
				print ('[$] Try to use proxy after fail.')
				randomProxy() #Check that, may contain bugs
			return False

		#return session if password is correct 
@@ -161,4 +166,3 @@ def Login(self, password):
		else:
			continue
