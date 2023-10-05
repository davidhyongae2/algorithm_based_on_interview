%possible structural biology question
t = [1,2,3]

theta = 30 
c = cos (theta)
s = sin (theta)

%mat*t = t'
%rotate on axis 
%https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/geometry/geo-tran.html#:~:text=A%20rotation%20matrix%20and%20a,rotations%20followed%20by%20a%20translation.
mat = [ (t(1) * t(1) * c) (t(1)*t(2) * (-s)) (t(1)*t(3) * s); (t(1)* t(2) * s) (t(2)*t(2) * c) (t(2)*t(3) *s); (t(1)*t(3) *s) (t(2)*t(3) * s) (t(3)*t(3) *c)]

