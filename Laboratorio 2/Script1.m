%% inicialización de ROS
rosinit; %conexion con nodo maestro

%% Inicialización de publisher y del mensaje
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %creacion del publisher al topico cmd_vel
velMsg = rosmessage(velPub); %creación del mensaje

%% Ejemplo de envío de un mensaje para desplazar la  tortuga empleando cmd_vel
velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envío
pause(1)

%% Sucripción al tópico de pose
poseSub = rossubscriber("/turtle1/pose",)