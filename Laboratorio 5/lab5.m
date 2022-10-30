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

%
