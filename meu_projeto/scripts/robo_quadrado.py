#! /usr/bin/env python
# -*- coding:utf-8 -*-


import rospy
import numpy as np
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan
i = 0

def scaneou(dado):
	print("Faixa valida: ", dado.range_min , " - ", dado.range_max )
	print("Leituras:")
	print(np.array(dado.ranges).round(decimals=2))
	#print("Intensities")
	#print(np.array(dado.intensities).round(decimals=2))

	


if __name__=="__main__":

	rospy.init_node("le_scan")

	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 1 )
	#recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)



	while not rospy.is_shutdown():
		while (i<14):
			print("Oeee")
			if (i<2):
				velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0,0))
				velocidade_saida.publish(velocidade)
			elif (i == 4):
				velocidade = Twist(Vector3(0,0,0), Vector3(0,0,0.8))
				velocidade_saida.publish(velocidade)
			elif (i>4 and i<6):
				velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0,0))
				velocidade_saida.publish(velocidade)

			elif (i == 6):
				velocidade = Twist(Vector3(0,0,0), Vector3(0,0,0.8))
				velocidade_saida.publish(velocidade)

			elif (i>6 and i<8):
				velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0,0))
				velocidade_saida.publish(velocidade)	

			elif (i == 8):
				velocidade = Twist(Vector3(0,0,0), Vector3(0,0,0.8))
				velocidade_saida.publish(velocidade)

			elif (i>8 and i<10):
				velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0,0))
				velocidade_saida.publish(velocidade)	

			elif (i == 10):
				velocidade = Twist(Vector3(0,0,0), Vector3(0,0,0.8))
				velocidade_saida.publish(velocidade)											
					
							
				

			else:
				velocidade = Twist(Vector3(0,0,0), Vector3(0,0,0))
				velocidade_saida.publish(velocidade)
			i += 1
			print (i)


			rospy.sleep(2)
