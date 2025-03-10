++++++++++			index 0 = 10
>					move to index 1
+++++++++++++++
+++++++++++++++
+++++++++++++++
+++					index 1 = 48 = '0'
<					move to index 0
[					starts a loop
	>.+				print and increment index 1
	<-				decrement and switch to index 0
]					stops the loop
++++++++++.			print '\n'
