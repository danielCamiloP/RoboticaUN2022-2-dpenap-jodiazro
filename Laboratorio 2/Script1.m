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
poseSub = rossubscriber("/turtle1/pose",'turtlesim/Pose'); %Creación del suscriptor
poseMsg = poseSub.LatestMessage; %Obtención del último mensaje del tópico PoseS
%% Envío de valores asociados a la pose de turtle1
%Para poder modificar la pose de la tortuga de manera directa, se deben
%emplear servicios, como lo indica la wiki de ros http://wiki.ros.org/turtlesim
%Hay dos maneras de cambiar la pose. El servicio teleport_absolute y
%teleport_relative. Como se indica en el nombre, uno permite emplear
%coordenadas absolutas mientras el otro permite usar coordenadas relativas.

%ejemplo con coordenadas absolutas

%ejemplo con coordenadas relativas


%% Finalización del nodo maestro de ROS
%Consultando la documentación de ROSToolbox, se debe ejecutar
rosshutdown;