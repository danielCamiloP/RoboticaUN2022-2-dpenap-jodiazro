L = [46 107 107 110];
DHParams = [0 L(1) 0 pi/2 0 0;
            0 0 L(2) 0 0 pi/2;
            0 0 L(3) 0 0 0;
            0 0 L(4) 0 0 0];            

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

q = pi/180*[0 0 0 0;
     -20 -20 -20 20;
     30 -30 30 -30;
     -90 15 -55 17;
     -90 45 -55 45;
     -45 45 45 45;
     0 0 -90 0;];

elem=4; %Se selecciona que posición se desea graficar.
%figure;
R.plot(q(elem,:),'noa')