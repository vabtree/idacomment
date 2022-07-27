// Clear all (anterior)comments by funcap using IDC

#include <idc.idc>
static main(void) {
	auto ea;
	for (ea=MinEA(); ea != BADADDR; ea=NextHead(ea, BADADDR))
	{
		DelExtLnA(ea, 0);  // delete anterior comments
		SetColor(ea, CIC_FUNC, DEFCOLOR);  // set default color of functions and data
		SetColor(ea, CIC_ITEM, DEFCOLOR);
	}
	Message("[*] refreshing disassembly.");
	Refresh();
	Message(".ok\n");
	Message("[*] refreshing lists.");
	RefreshLists();
	Message(".ok\n");
}
