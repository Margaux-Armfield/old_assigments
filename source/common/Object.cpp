//////////////////////////////////////////////////////////////////////////////
//
//  --- Object.cpp ---
//  Created by Brian Summa
//
//////////////////////////////////////////////////////////////////////////////


#include "common.h"

/* -------------------------------------------------------------------------- */
/* -------------------------------------------------------------------------- */
Object::IntersectionValues Sphere::intersect(vec4 p0_w, vec4 V_w){
    vec4 P_o;
    double t_o;
    vec4 N_o;
    IntersectionValues result;
    vec4 p0_o = INVC*p0_w;
    vec4 V_o = INVCStar*V_w;
    double len = length(V_o);
    V_o = normalize(V_o);
 
    //TODO: Ray-sphere setup
    
    t_o = raySphereIntersection(p0_o, V_o);
    result.t_w = t_o/len;
    result.P_w = p0_w + result.t_w*V_w;
    P_o = p0_o + t_o*V_o;
       P_o = normalize(P_o);
    N_o = P_o;
    N_o.w = 0.0;
    N_o = normalize(N_o);
    
    result.N_w = TRANINVC*N_o;
    
    result.N_w.w = 0.0;
    result.N_w = normalize(result.N_w);
    
  return result;
}

/* -------------------------------------------------------------------------- */
/* ------ Ray = p0 + t*V  sphere at origin O and radius r    : Find t ------- */
double Sphere::raySphereIntersection(vec4 p0, vec4 V, vec4 O, double r){
  double t   = std::numeric_limits< double >::infinity();
  //TODO: Ray-sphere intersection;
    double a = 1.0;
    double b = dot(2*V, p0-vec4(0,0,0,1));
    double c = pow(length(p0-vec4(0,0,0,1)),2) - pow(r, 2);
    
    if ((b*b-4*a*c)< 0) {
        return t;
    }
    double t1 = (-b + sqrt(b*b-4*a*c))/2*a;
    double t2 = (-b - sqrt(b*b-4*a*c))/2*a;
    
    if(t1< EPSILON){ t1 = std::numeric_limits< double >::infinity(); }
    if(t2< EPSILON){ t2 = std::numeric_limits< double >::infinity(); }
    return fmin(t1, t2);


  return t;
}

/* -------------------------------------------------------------------------- */
/* -------------------------------------------------------------------------- */
Object::IntersectionValues Square::intersect(vec4 p0_w, vec4 V_w){
    vec4 P_o;
    double t_o;
    vec4 N_o;
    IntersectionValues result;
    vec4 p0_o = INVC*p0_w;
    vec4 V_o = INVCStar*V_w;
    double len = length(V_o);
    V_o = normalize(V_o);
    
    //TODO: Ray-sphere setup
    
    t_o = raySquareIntersection(p0_o, V_o);
    result.t_w = t_o/len;
    result.P_w = p0_w + result.t_w * V_w;
    P_o = p0_o + t_o*V_o;
  //  P_o = normalize(P_o);
    N_o = vec4(0,0,1,0);
    
    result.N_w = TRANINVC * N_o;
    
    result.N_w.w = 0.0;
    result.N_w = normalize(result.N_w);
 
    return result;
}

/* -------------------------------------------------------------------------- */
/* -------------------------------------------------------------------------- */
double Square::raySquareIntersection(vec4 p0, vec4 V){
  double t   = std::numeric_limits< double >::infinity();
    vec4 P_o;
    double t1;
    vec4 N = vec4(0,0,1,0);
    
    //TODO: Ray-square intersection;
    //t= N·(S–P1)/N·(P2–P1)
    if (dot(N, V)==0) {
        return t;
    }
    t1 = dot(N, (vec4(0,0,0,1)-p0))/(dot(N, V));
    if (t1 < EPSILON) {
        return t;
    }

    P_o = p0+ t1*V;
    if (P_o.x > 1+EPSILON || P_o.x < -1 - EPSILON) {
        return t;
    }
    if (P_o.y > 1+EPSILON || P_o.y < -1 - EPSILON) {
        return t;
    }
  return t1;
}
