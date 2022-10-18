%% Inicialización del workspace
clc;
clear;
close all;
startup_rvc;
%% Parametrización del Phantom X
L = [46 107 107 110];
DHParams = [0 L(1) 0 sym(pi)/2;
            0 0 L(2) 0;
            0 0 L(3) 0;
            0 0 L(4) 0];            

Lnk(1) = Link(DHParams(1,:));
Lnk(2) = Link(DHParams(2,:));
Lnk(3) = Link(DHParams(3,:));
Lnk(4) = Link(DHParams(4,:));


R = SerialLink(Lnk,'name','PhantomX');

H_tool = [0 0 1 0;
          1 0 0 0;
          0 1 0 0;
          0 0 0 1];

R.tool = H_tool;

syms q [1 4]
R.fkine(q)

%% Grafica de las posiciones
figure
R.plot([0 0 0 0],'noa')
figure
R.plot(pi/180*[-20 -20 -20 20],'noa')

figure
R.plot(pi/180*[30 -30 30 -30],'noa')

figure
R.plot(pi/180*[-90 15 -55 17],'noa')

figure
R.plot(pi/180*[-90 45 -55 45],'noa')