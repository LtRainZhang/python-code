clear all;
path = './test.xyz';
file = fopen(path,'r');
num = 208; % total atom number
timestep = 0.5; % MD time step
n1 = 10000;  % initial position
n2 = 19999;  % final position equal to max tryjectory    n2 >=2 && n2 >=n1
for hh = n1:n2
    if hh == n1
        B = textscan(file,'%s %f %f %f',num,'HeaderLines',2+(n1-1)*(num+2));
        p = 1;
        for i = 1:num
            if strcmp(B{1}{i},'Si')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        num_Si = p-1;
        for i = 1:num
            if strcmp(B{1}{i},'O')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        num_O = p - 1 - num_Si;
        for i = 1:num
            if strcmp(B{1}{i},'Li')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        num_Li = p - 1 - num_Si - num_O;
        for i = 1:num
            if strcmp(B{1}{i},'Al')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        num_Al = p - 1 - num_Si - num_O - num_Li;
        for i = 1:num
            if strcmp(B{1}{i},'Na')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        num_Na = p - 1 - num_Si - num_O - num_Li - num_Al;
        eval(['cor_',num2str(hh),'=A',';'])
    else
        B = textscan(file,'%s %f %f %f',num,'HeaderLines',3);
         p = 1;
        for i = 1:num
            if strcmp(B{1}{i},'Si')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        for i = 1:num
            if strcmp(B{1}{i},'O')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        for i = 1:num
            if strcmp(B{1}{i},'Li')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        for i = 1:num
            if strcmp(B{1}{i},'Al')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        num_Al = p - 1 - num_Si - num_O - num_Li;
        for i = 1:num
            if strcmp(B{1}{i},'Na')~=0
                A{p,1}=B{1}{i};
                A{p,2}=B{2}(i);
                A{p,3}=B{3}(i);
                A{p,4}=B{4}(i);
                p = p + 1;
            end
        end
        num_Na = p - 1 - num_Si - num_O - num_Li - num_Al;
        eval(['cor_',num2str(hh),'=A',';'])
    end
end

fclose(file);
%  eval(['num_', species{i}, ' = ' num2str(0)]);



t = 1;
for i = 1:(n2-n1)
    init = n1;
    autocorr = n1 + t;
    msd_Si = 0;
    msd_O = 0;
    msd_Li = 0;
    msd_Al = 0;
    msd_Na = 0;
    for j = 1:n2-n1-t+1
        %  define initial atom position
        eval(['init_cor','=','cor_',num2str(init),';'])
        %  define autocorrelate atom position
        eval(['final_cor','=','cor_',num2str(autocorr),';'])
        for k = 1:num_Si       % msd_Si
            x1 = init_cor{k,2};
            x2 = final_cor{k,2};
            y1 = init_cor{k,3};
            y2 = final_cor{k,3};
            z1 = init_cor{k,4};
            z2 = final_cor{k,4};
            msd_Si = msd_Si + (x1-x2)^2+(y1-y2)^2+(z1-z2)^2;
        end
        
        for k = (1+num_Si):(num_Si+num_O)  %msd_O
            x1 = init_cor{k,2};
            x2 = final_cor{k,2};
            y1 = init_cor{k,3};
            y2 = final_cor{k,3};
            z1 = init_cor{k,4};
            z2 = final_cor{k,4};
            msd_O = msd_O + (x1-x2)^2+(y1-y2)^2+(z1-z2)^2;
        end
        
        for k = (1+num_Si+num_O):(num_Si+num_O+num_Li)   %msd_Li
            x1 = init_cor{k,2};
            x2 = final_cor{k,2};
            y1 = init_cor{k,3};
            y2 = final_cor{k,3};
            z1 = init_cor{k,4};
            z2 = final_cor{k,4};
            msd_Li = msd_Li + (x1-x2)^2+(y1-y2)^2+(z1-z2)^2;
        end
        
        for k = (1+num_Si+num_O+num_Li):(num_Si+num_O+num_Li+num_Al)   %msd_Li
            x1 = init_cor{k,2};
            x2 = final_cor{k,2};
            y1 = init_cor{k,3};
            y2 = final_cor{k,3};
            z1 = init_cor{k,4};
            z2 = final_cor{k,4};
            msd_Al = msd_Al + (x1-x2)^2+(y1-y2)^2+(z1-z2)^2;
        end
        
        for k = (num_Si+num_O+num_Li+num_Al):(num_Si+num_O+num_Li+num_Al+num_Na)   %msd_Li
            x1 = init_cor{k,2};
            x2 = final_cor{k,2};
            y1 = init_cor{k,3};
            y2 = final_cor{k,3};
            z1 = init_cor{k,4};
            z2 = final_cor{k,4};
            msd_Na = msd_Na + (x1-x2)^2+(y1-y2)^2+(z1-z2)^2;
        end
        
        init = init + 1;
        autocorr = autocorr + 1;
    end
    msd_Siconvert = msd_Si/(num_Si * (n2-n1-t+1));
    msd_Oconvert = msd_O/(num_O * (n2-n1-t+1));
    msd_Liconvert = msd_Li/(num_Li * (n2-n1-t+1));
    msd_Alconvert = msd_Al/(num_Al * (n2-n1-t+1));
    msd_Naconvert = msd_Na/(num_Na * (n2-n1-t+1));
    
    msd_Sifinal(t,1) = t * timestep * 100 / 1000;
    msd_Sifinal(t,2) = msd_Siconvert;
    msd_Ofinal(t,1) = t * timestep * 100 / 1000;
    msd_Ofinal(t,2) = msd_Oconvert;
    msd_Lifinal(t,1) = t * timestep * 100 / 1000;
    msd_Lifinal(t,2) = msd_Liconvert;
    msd_Alfinal(t,1) = t * timestep * 100 / 1000;
    msd_Alfinal(t,2) = msd_Alconvert;
    msd_Nafinal(t,1) = t * timestep * 100 / 1000;
    msd_Nafinal(t,2) = msd_Naconvert;
    
    t = t + 1;
    disp(t);
end
path1 = './msd.data';
fp1 = fopen(path1,'w');
fprintf(fp1,'time   MSD-Si   MSD-O   MSD-Li   MSD-Al   MSD-Na\r\n');
for i = 1:(t-1)
    
   fprintf(fp1,'%8.6f   %8.6f   %8.6f   %8.6f   %8.6f   %8.6f\r\n',msd_Sifinal(i,1), msd_Sifinal(i,2),msd_Ofinal(i,2),msd_Lifinal(i,2),msd_Alfinal(i,2),msd_Nafinal(i,2));
end





