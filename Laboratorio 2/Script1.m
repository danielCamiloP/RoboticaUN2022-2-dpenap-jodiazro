%% Reinicio de variables y consola
clc;
clear;

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
poseMsg = poseSub.LatestMessage %Obtención del último mensaje del tópico PoseS
%% Envío de valores asociados a la pose de turtle1
%Para poder modificar la pose de la tortuga de manera directa, se deben
%emplear servicios, como lo indica la wiki de ros http://wiki.ros.org/turtlesim
%Hay dos maneras de cambiar la pose. El servicio teleport_absolute y
%teleport_relative. Como se indica en el nombre, uno permite emplear
%coordenadas absolutas mientras el otro permite usar coordenadas relativas.

%%ejemplo con coordenadas absolutas
%creación del cliente
clAbs = rossvcclient('/turtle1/teleport_absolute');
msgAbs = rosmessage(clAbs);

% Asignación de valores
msgAbs.X = 5; %mover la tortuga a x=5
msgAbs.Y = 8; %mover la tortuga a y=8
msgAbs.Theta = (3/5) *pi; %hacer que la tortuga rote hasta 3pi/5

%envio al cliente
responseAbs = call(clAbs,msgAbs);
pause(1);

% Como se puede ver, la sintaxis es muy similar a emplear un publisher.

%% ejemplo con coordenadas relativas
clRel = rossvcclient('/turtle1/teleport_relative');
msgRel = rosmessage(clRel);

% Asignación de valores
msgRel.Linear = 3; %avanzar 3 unidades hacia donde apunta la tortuga
msgRel.Angular = pi/2; %rotar la tortuga pi/2 rad

%envio al cliente
responseRel = call(clRel,msgRel);
pause(1);

%Si se corre 4 veces este código la tortuga realizará un cuadrado desde su
%posición en el momento de ejecutar la sección por primera vez
%% Finalización del nodo maestro de ROS
%Consultando la documentación de ROSToolbox, se debe ejecutar
rosshutdown;