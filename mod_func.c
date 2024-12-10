#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _CaT_reg();
extern void _ca_reg();
extern void _cad_reg();
extern void _cagk_reg();
extern void _carF_reg();
extern void _car_new_reg();
extern void _exp2synNMDA_reg();
extern void _id_reg();
extern void _kad_reg();
extern void _kap_reg();
extern void _kca_reg();
extern void _kdr_reg();
extern void _km_reg();
extern void _kslow_new_reg();
extern void _kv_reg();
extern void _na_reg();
extern void _nadend_reg();
extern void _nax_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," CaT.mod");
fprintf(stderr," ca.mod");
fprintf(stderr," cad.mod");
fprintf(stderr," cagk.mod");
fprintf(stderr," carF.mod");
fprintf(stderr," car_new.mod");
fprintf(stderr," exp2synNMDA.mod");
fprintf(stderr," id.mod");
fprintf(stderr," kad.mod");
fprintf(stderr," kap.mod");
fprintf(stderr," kca.mod");
fprintf(stderr," kdr.mod");
fprintf(stderr," km.mod");
fprintf(stderr," kslow_new.mod");
fprintf(stderr," kv.mod");
fprintf(stderr," na.mod");
fprintf(stderr," nadend.mod");
fprintf(stderr," nax.mod");
fprintf(stderr, "\n");
    }
_CaT_reg();
_ca_reg();
_cad_reg();
_cagk_reg();
_carF_reg();
_car_new_reg();
_exp2synNMDA_reg();
_id_reg();
_kad_reg();
_kap_reg();
_kca_reg();
_kdr_reg();
_km_reg();
_kslow_new_reg();
_kv_reg();
_na_reg();
_nadend_reg();
_nax_reg();
}
