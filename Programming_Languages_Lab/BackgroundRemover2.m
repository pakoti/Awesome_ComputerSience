S='';
I=imread(S);

Figure(1);
imshow(I);
figure(2);

idx1=((I(:,:,1) > 107 & I(:,:,1) > 209));
idx2=((I(:,:,2) > 107 & I(:,:,1) > 209));
idx3=((I(:,:,3) > 107 & I(:,:,1) > 209));

IDX=idx1 .* idx2 .* idx3 ;

sum(sum(sum(IDX)));

I2=I;



