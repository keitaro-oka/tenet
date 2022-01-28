2 1
{S[n,k,c,ox,oy,rx,ry]:0<=n<1 and 0<=k<64 and 0<=c<3 and 0<=ox<128 and 0<=oy<128 and 0<=rx<3 and 0<=ry<3}
{S[n,k,c,ox,oy,rx,ry]->I[n,c,ox*1+rx,oy*1+ry]}
{S[n,k,c,ox,oy,rx,ry]->W[k,c,rx,ry]}
{S[n,k,c,ox,oy,rx,ry]->O[n,k,ox,oy]}
