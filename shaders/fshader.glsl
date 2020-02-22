#version 150
uniform vec4 AmbientProduct;
uniform vec4 DiffuseProduct;
uniform vec4 SpecularProduct;
uniform vec4 LightPosition;
uniform float Shininess;

uniform mat4 ModelViewLight;

in vec4 pos;
in vec4 N;

out vec4 fragColor;

void main()
{
    
    vec4 L;
    if(LightPosition.w == 0.0){
        L = normalize(LightPosition - pos); L.w = 0;
    }else{
        L = normalize((ModelViewLight*LightPosition) - pos ); L.w = 0;
    }
    
    vec4 V = normalize( -pos);  V.w = 0.0;
    vec4 R = normalize(-reflect(L,N));
    
    // Compute terms in the illumination equation
    vec4 ambient = AmbientProduct;
    
    float Kd = max( dot(L, N), 0.0 );
    vec4  diffuse = Kd*DiffuseProduct;
    
    float Ks = pow( max(dot(V, R), 0.0), Shininess );
    
    //Phong/Blinn used the half angle approx:
    //float Ks = pow( max(dot(N, normalize( L + V ) ), 0.0), Shininess );
    
    vec4  specular = Ks * SpecularProduct;
    
    if( dot(L, N) < 0.0 ) {
        fragColor = vec4(0.0, 0.0, 0.0, 1.0);
    }else{
        fragColor = ambient + diffuse + specular;
    }
    
}

//uniform vec4 AmbientProduct;
//uniform vec4 DiffuseProduct;
//uniform vec4 SpecularProduct;
//uniform vec4 LightPosition;
//uniform float Shininess;
//
//in vec4 pos;
//in vec4 N;
//
//out vec4 fragColor;
//
//void main()
//{
//
//  // Ambient
//  vec4 ambient = (0.5,0.5,0.5) * AmbientProduct;
//
//  // Diffuse
//  //Id =Ii(L⋅N)
// float D  = max(0,dot(LightPosition,N));
//
//  vec4  diffuse = D * DiffuseProduct;
//
//  //Specular
//  // Is =Ii(R⋅V)^n
//  // Use reflect function to find the reflection of light about the normal (make negative so its the right direction)
//  vec4 R = -reflect(LightPosition,N);
//
//  // V is for viewer, which you calculate as Eye - position. Since E is at the origin (0,0,0,1), V = - pos
//  vec4 V = -pos;
//  V.w = 0;
//
//  // Vectors aren't guarenteed to be normal, so normalize them
//  R = normalize(R);
//  V = normalize(V);
//
//  // use max function in case dot product is negative
//  float S = max(0,pow(dot(V,R),Shininess));
//
//  vec4  specular = S * SpecularProduct;
//
//  fragColor = ambient + diffuse + specular;
//}
//
