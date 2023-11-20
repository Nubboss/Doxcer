from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Empl(models.Model):
    idempl = models.IntegerField(db_column='IdEmpl', unique=True)  # Field name made lowercase.
    uguid = models.CharField(db_column='uGUID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ucomp = models.CharField(db_column='uComp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ustatus = models.IntegerField(db_column='uStatus')  # Field name made lowercase.
    namee = models.CharField(db_column='NameE', primary_key=True,
                             max_length=30)  # Field name made lowercase. The composite primary key (NameE, NameE2, NameE3, IdDep, PostE) found, that is not supported. The first column is selected.
    namee2 = models.CharField(db_column='NameE2', max_length=30)  # Field name made lowercase.
    namee3 = models.CharField(db_column='NameE3', max_length=30)  # Field name made lowercase.
    nameerp = models.CharField(db_column='NameERP', max_length=35, blank=True, null=True)  # Field name made lowercase.
    poste = models.CharField(db_column='PostE', max_length=85)  # Field name made lowercase.
    postesign = models.CharField(db_column='PostESign', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    iddep = models.IntegerField(db_column='IdDep')  # Field name made lowercase.
    staffer = models.IntegerField(db_column='Staffer')  # Field name made lowercase.
    chieftrue = models.IntegerField(db_column='ChiefTrue', blank=True, null=True)  # Field name made lowercase.
    chiefchtrue = models.IntegerField(db_column='ChiefChTrue', blank=True, null=True)  # Field name made lowercase.
    chiefaitrue = models.IntegerField(db_column='ChiefAITrue', blank=True, null=True)  # Field name made lowercase.
    dismtrue = models.IntegerField(db_column='DismTrue', blank=True, null=True)  # Field name made lowercase.
    periph = models.IntegerField(db_column='Periph')  # Field name made lowercase.
    condexp = models.IntegerField(db_column='CondExp')  # Field name made lowercase.
    nameee = models.CharField(db_column='NameEE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nameee2 = models.CharField(db_column='NameEE2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nameee3 = models.CharField(db_column='NameEE3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dide = models.CharField(db_column='DidE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tele = models.CharField(db_column='TelE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    emaile = models.CharField(db_column='EmailE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sortnum = models.IntegerField(db_column='SortNum', blank=True, null=True)  # Field name made lowercase.
    emplform = models.CharField(db_column='EmplForm', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    emplspec = models.CharField(db_column='EmplSpec', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    emplpost = models.CharField(db_column='EmplPost', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    emplwork = models.CharField(db_column='EmplWork', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    emplexp = models.CharField(db_column='EmplExp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datebirth = models.DateField(db_column='DateBirth', blank=True, null=True)  # Field name made lowercase.
    prper1 = models.FloatField(db_column='PrPer1')  # Field name made lowercase.
    prper2 = models.FloatField(db_column='PrPer2')  # Field name made lowercase.
    shweba = models.IntegerField(db_column='ShWebA')  # Field name made lowercase.
    shwebp = models.IntegerField(db_column='ShWebP')  # Field name made lowercase.
    shmes = models.IntegerField(db_column='ShMes')  # Field name made lowercase.
    signfile = models.CharField(db_column='SignFile', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    signcoef = models.FloatField(db_column='SignCoef')  # Field name made lowercase.
    signdeltacalc = models.FloatField(db_column='SignDeltaCalc')  # Field name made lowercase.
    usesignchief = models.IntegerField(db_column='UseSignChief')  # Field name made lowercase.
    usesignchiefnord = models.CharField(db_column='UseSignChiefNOrd', max_length=20, blank=True,
                                        null=True)  # Field name made lowercase.
    usesignforchiefnord = models.CharField(db_column='UseSignForChiefNOrd', max_length=20, blank=True,
                                           null=True)  # Field name made lowercase.
    usesignforchacnord = models.CharField(db_column='UseSignForChAcNOrd', max_length=20, blank=True,
                                          null=True)  # Field name made lowercase.
    e_sign_cert_thumbprint = models.CharField(db_column='E_Sign_Cert_Thumbprint', max_length=100, blank=True,
                                              null=True)  # Field name made lowercase.
    numbserv = models.IntegerField(db_column='NumbServ')  # Field name made lowercase.
    usersdb = models.CharField(db_column='UsersDb', max_length=30)  # Field name made lowercase.
    compusers = models.CharField(db_column='CompUsers', max_length=30)  # Field name made lowercase.
    datetimech = models.DateTimeField(db_column='DateTimeCh')  # Field name made lowercase.
    nscreator = models.IntegerField(db_column='NSCreator')  # Field name made lowercase.
    idel = models.IntegerField(db_column='iDel')  # Field name made lowercase.
    idpostch = models.IntegerField(db_column='IdPostCh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empl'
        unique_together = (('namee', 'namee2', 'namee3', 'iddep', 'poste'),)


class Firms(models.Model):
    idfirm = models.IntegerField(db_column='IdFirm', primary_key=True)  # Field name made lowercase.
    namef = models.CharField(db_column='NameF', max_length=255)  # Field name made lowercase.
    namefab = models.CharField(db_column='NameFAb', max_length=120, blank=True, null=True)  # Field name made lowercase.
    namefen = models.CharField(db_column='NameFEN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datecr = models.DateField(db_column='DateCr', blank=True, null=True)  # Field name made lowercase.
    notifcr = models.IntegerField(db_column='NotifCr')  # Field name made lowercase.
    nameolf = models.CharField(db_column='NameOLF', max_length=70, blank=True, null=True)  # Field name made lowercase.
    nameolfen = models.CharField(db_column='NameOLFEN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nameolffn = models.CharField(db_column='NameOLFFN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nametype = models.CharField(db_column='NameType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    typebus = models.IntegerField(db_column='TypeBus', blank=True, null=True)  # Field name made lowercase.
    mailind = models.CharField(db_column='MailInd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fcntr = models.CharField(db_column='FCntr', max_length=100)  # Field name made lowercase.
    fcntrfn = models.CharField(db_column='FCntrFN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    freg = models.CharField(db_column='FReg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    farea = models.CharField(db_column='FArea', max_length=100, blank=True, null=True)  # Field name made lowercase.
    focc = models.CharField(db_column='FOcc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    foccs = models.CharField(db_column='FOccS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    faddr = models.CharField(db_column='FAddr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addrfen = models.CharField(db_column='AddrFEN', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ftelc = models.CharField(db_column='FTelC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mailindl = models.CharField(db_column='MailIndL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fcntrl = models.CharField(db_column='FCntrL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fcntrfnl = models.CharField(db_column='FCntrFNL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fregl = models.CharField(db_column='FRegL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fareal = models.CharField(db_column='FAreaL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    foccl = models.CharField(db_column='FOccL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    foccsl = models.CharField(db_column='FOccSL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    faddrl = models.CharField(db_column='FAddrL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ftelcl = models.CharField(db_column='FTelCL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amwork = models.IntegerField(db_column='AmWork', blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kpp = models.CharField(db_column='KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    kpp2 = models.CharField(db_column='KPP2', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ogrn = models.CharField(db_column='OGRN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telspl = models.CharField(db_column='TelSpl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=255, blank=True, null=True)  # Field name made lowercase.
    faxspl = models.CharField(db_column='FaxSpl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    web = models.CharField(db_column='Web', max_length=255, blank=True, null=True)  # Field name made lowercase.
    logfile = models.CharField(db_column='LogFile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logtext = models.TextField(db_column='LogText', blank=True, null=True)  # Field name made lowercase.
    postch = models.CharField(db_column='PostCh', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chief = models.CharField(db_column='Chief', max_length=30, blank=True, null=True)  # Field name made lowercase.
    chief2 = models.CharField(db_column='Chief2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    chief3 = models.CharField(db_column='Chief3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cheifactsbasis = models.CharField(db_column='CheifActsBasis', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datebirth = models.DateField(db_column='DateBirth', blank=True, null=True)  # Field name made lowercase.
    notifbirth = models.IntegerField(db_column='NotifBirth')  # Field name made lowercase.
    telchief = models.CharField(db_column='TelChief', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postrp = models.CharField(db_column='PostRP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chrp = models.CharField(db_column='ChRP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    chrp2 = models.CharField(db_column='ChRP2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    chrp3 = models.CharField(db_column='ChRP3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankaddr = models.CharField(db_column='BankAddr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accsc = models.CharField(db_column='AccSc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    corsc = models.CharField(db_column='CorSc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bik = models.CharField(db_column='Bik', max_length=9, blank=True, null=True)  # Field name made lowercase.
    okpo = models.CharField(db_column='Okpo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    okonh = models.CharField(db_column='Okonh', max_length=500, blank=True, null=True)  # Field name made lowercase.
    prim = models.TextField(db_column='Prim', blank=True, null=True)  # Field name made lowercase.
    membch = models.IntegerField(db_column='MembCh', blank=True, null=True)  # Field name made lowercase.
    membch_ch = models.IntegerField(db_column='MembCh_Ch', blank=True, null=True)  # Field name made lowercase.
    dateint_ch = models.DateField(db_column='DateInt_Ch', blank=True, null=True)  # Field name made lowercase.
    ntick_ch = models.CharField(db_column='NTick_Ch', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateexp_ch = models.DateField(db_column='DateExp_Ch', blank=True, null=True)  # Field name made lowercase.
    contrib_ch = models.FloatField(db_column='Contrib_Ch', blank=True, null=True)  # Field name made lowercase.
    membch_mg = models.IntegerField(db_column='MembCh_Mg', blank=True, null=True)  # Field name made lowercase.
    dateint_mg = models.DateField(db_column='DateInt_Mg', blank=True, null=True)  # Field name made lowercase.
    ntick_mg = models.CharField(db_column='NTick_Mg', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateexp_mg = models.DateField(db_column='DateExp_Mg', blank=True, null=True)  # Field name made lowercase.
    contrib_mg = models.FloatField(db_column='Contrib_Mg', blank=True, null=True)  # Field name made lowercase.
    membch_ms = models.IntegerField(db_column='MembCh_Ms', blank=True, null=True)  # Field name made lowercase.
    dateint_ms = models.DateField(db_column='DateInt_Ms', blank=True, null=True)  # Field name made lowercase.
    ntick_ms = models.CharField(db_column='NTick_Ms', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateexp_ms = models.DateField(db_column='DateExp_Ms', blank=True, null=True)  # Field name made lowercase.
    contrib_ms = models.FloatField(db_column='Contrib_Ms', blank=True, null=True)  # Field name made lowercase.
    datestreg = models.DateField(db_column='DateStReg', blank=True, null=True)  # Field name made lowercase.
    nregcert = models.CharField(db_column='NRegCert', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orgprcert = models.CharField(db_column='OrgPrCert', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postresp = models.CharField(db_column='PostResp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resp = models.CharField(db_column='Resp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telrp = models.CharField(db_column='TelRP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primmch = models.TextField(db_column='PrimMCh', blank=True, null=True)  # Field name made lowercase.
    dutymemb = models.IntegerField(db_column='DutyMemb', blank=True, null=True)  # Field name made lowercase.
    invitmemb = models.IntegerField(db_column='InvitMemb', blank=True, null=True)  # Field name made lowercase.
    dateinvit = models.DateField(db_column='DateInvit', blank=True, null=True)  # Field name made lowercase.
    datereg = models.DateField(db_column='DateReg', blank=True, null=True)  # Field name made lowercase.
    membruz = models.IntegerField(db_column='MembRUZ')  # Field name made lowercase.
    ntickruz = models.CharField(db_column='NTickRUZ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dateintruz = models.DateField(db_column='DateIntRUZ', blank=True, null=True)  # Field name made lowercase.
    dateexpruz = models.DateField(db_column='DateExpRUZ', blank=True, null=True)  # Field name made lowercase.
    emailruz = models.CharField(db_column='EmailRUZ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fns_datetime = models.DateTimeField(db_column='FNS_DateTime', blank=True, null=True)  # Field name made lowercase.
    fns_status = models.CharField(db_column='FNS_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fns_ogrn = models.CharField(db_column='FNS_OGRN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fns_inn = models.CharField(db_column='FNS_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    fns_kpp = models.CharField(db_column='FNS_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    fns_nameolffn = models.CharField(db_column='FNS_NameOLFFN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fns_nameolf = models.CharField(db_column='FNS_NameOLF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fns_namef = models.CharField(db_column='FNS_NameF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fns_namefab = models.CharField(db_column='FNS_NameFAb', max_length=120, blank=True, null=True)  # Field name made lowercase.
    fns_mailind = models.CharField(db_column='FNS_MailInd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fns_fcntrfn = models.CharField(db_column='FNS_FCntrFN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fns_freg = models.CharField(db_column='FNS_FReg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fns_farea = models.CharField(db_column='FNS_FArea', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fns_focc = models.CharField(db_column='FNS_FOcc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fns_foccs = models.CharField(db_column='FNS_FOccS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fns_postch = models.CharField(db_column='FNS_PostCh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fns_chief = models.CharField(db_column='FNS_Chief', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fns_chief2 = models.CharField(db_column='FNS_Chief2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fns_chief3 = models.CharField(db_column='FNS_Chief3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fns_faddr = models.CharField(db_column='FNS_FAddr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numbserv = models.IntegerField(db_column='NumbServ')  # Field name made lowercase.
    usersdb = models.CharField(db_column='UsersDb', max_length=30)  # Field name made lowercase.
    compusers = models.CharField(db_column='CompUsers', max_length=30)  # Field name made lowercase.
    datetimech = models.DateTimeField(db_column='DateTimeCh')  # Field name made lowercase.
    nscreator = models.IntegerField(db_column='NSCreator')  # Field name made lowercase.
    idel = models.IntegerField(db_column='iDel')  # Field name made lowercase.
    aut_doc = models.CharField(max_length=30)
    ar_all_view = models.IntegerField()
    ar_all_edit = models.IntegerField()
    ar_gov_view = models.IntegerField()
    ar_gov_edit = models.IntegerField()
    ar_div_view = models.IntegerField()
    ar_div_edit = models.IntegerField()
    ar_aut_view = models.IntegerField()
    ar_aut_edit = models.IntegerField()
    idocc = models.IntegerField(db_column='IdOcc', blank=True, null=True)  # Field name made lowercase.
    idolf = models.IntegerField(db_column='IdOLF', blank=True, null=True)  # Field name made lowercase.
    idoccl = models.IntegerField(db_column='IdOccL', blank=True, null=True)  # Field name made lowercase.
    idbank = models.IntegerField(db_column='IdBank', blank=True, null=True)  # Field name made lowercase.
    dateact = models.DateField(db_column='DateAct', blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(max_length=255, blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    dateint = models.DateField(db_column='DateInt', blank=True, null=True)  # Field name made lowercase.
    ntick = models.CharField(db_column='NTick', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'firms'
        db_table_comment = 'InnoDB free: 154624 kB; InnoDB free: 160768 kB'



class Cact719(models.Model):
    numbact = models.CharField(db_column='NumbAct', primary_key=True, max_length=20)  # Field name made lowercase.
    numba = models.CharField(db_column='NumbA', max_length=15, blank=True, null=True)  # Field name made lowercase.
    yeara = models.CharField(db_column='YearA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    numbch = models.CharField(db_column='NumbCh', max_length=2, blank=True, null=True)  # Field name made lowercase.
    idcustexp = models.IntegerField(db_column='IdCustExp', blank=True, null=True)  # Field name made lowercase.
    custexp = models.CharField(db_column='CustExp', max_length=500, blank=True, null=True)  # Field name made lowercase.
    custexp_namef = models.CharField(db_column='CustExp_NameF', max_length=500, blank=True,
                                     null=True)  # Field name made lowercase.
    custexp_inn = models.CharField(db_column='CustExp_INN', max_length=12, blank=True,
                                   null=True)  # Field name made lowercase.
    custexp_kpp = models.CharField(db_column='CustExp_KPP', max_length=9, blank=True,
                                   null=True)  # Field name made lowercase.
    custexp_ogrn = models.CharField(db_column='CustExp_OGRN', max_length=15, blank=True,
                                    null=True)  # Field name made lowercase.
    custexp_addr = models.CharField(db_column='CustExp_Addr', max_length=500, blank=True,
                                    null=True)  # Field name made lowercase.
    custexp_addr_pa = models.CharField(db_column='CustExp_Addr_PA', max_length=500, blank=True,
                                       null=True)  # Field name made lowercase.
    empltextp = models.CharField(db_column='EmplTextP', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    empltext = models.CharField(db_column='EmplText', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    empltextp2 = models.CharField(db_column='EmplTextP2', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    empltext2 = models.CharField(db_column='EmplText2', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    empltextp3 = models.CharField(db_column='EmplTextP3', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    empltext3 = models.CharField(db_column='EmplText3', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    empltextp4 = models.CharField(db_column='EmplTextP4', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    empltext4 = models.CharField(db_column='EmplText4', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    empltextp5 = models.CharField(db_column='EmplTextP5', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    empltext5 = models.CharField(db_column='EmplText5', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    empltextp6 = models.CharField(db_column='EmplTextP6', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    empltext6 = models.CharField(db_column='EmplText6', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    dateact = models.DateField(db_column='DateAct')  # Field name made lowercase.
    dateterm = models.DateField(db_column='DateTerm', blank=True, null=True)  # Field name made lowercase.
    dateactp = models.DateField(db_column='DateActP', blank=True, null=True)  # Field name made lowercase.
    dateactp2 = models.DateField(db_column='DateActP2', blank=True, null=True)  # Field name made lowercase.
    desg = models.TextField(db_column='DesG', blank=True, null=True)  # Field name made lowercase.
    desgfile = models.CharField(db_column='DesGFile', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    desgshort = models.TextField(db_column='DesGShort', blank=True, null=True)  # Field name made lowercase.
    desgp = models.TextField(db_column='DesGP', blank=True, null=True)  # Field name made lowercase.
    docfile2 = models.CharField(db_column='DocFile2', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    idmanuf = models.IntegerField(db_column='IdManuf', blank=True, null=True)  # Field name made lowercase.
    manuf = models.TextField(db_column='Manuf', blank=True, null=True)  # Field name made lowercase.
    conclvar = models.IntegerField(db_column='ConclVar')  # Field name made lowercase.
    conclvar2 = models.IntegerField(db_column='ConclVar2')  # Field name made lowercase.
    concla = models.TextField(db_column='ConclA', blank=True, null=True)  # Field name made lowercase.
    conclafile = models.CharField(db_column='ConclAFile', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    concl = models.TextField(db_column='Concl', blank=True, null=True)  # Field name made lowercase.
    docfile3 = models.CharField(db_column='DocFile3', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    basex = models.CharField(db_column='BasEx', max_length=500, blank=True, null=True)  # Field name made lowercase.
    contr = models.TextField(db_column='Contr', blank=True, null=True)  # Field name made lowercase.
    contrfile = models.CharField(db_column='ContrFile', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    expest = models.TextField(db_column='ExpEst', blank=True, null=True)  # Field name made lowercase.
    expestfile = models.CharField(db_column='ExpEstFile', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    add_01_file = models.CharField(db_column='Add_01_File', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    add_01_date = models.DateField(db_column='Add_01_Date', blank=True, null=True)  # Field name made lowercase.
    add_01_empl = models.CharField(db_column='Add_01_Empl', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    add_01_datetime = models.DateTimeField(db_column='Add_01_DateTime', blank=True,
                                           null=True)  # Field name made lowercase.
    add_02_file = models.CharField(db_column='Add_02_File', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    add_02_date = models.DateField(db_column='Add_02_Date', blank=True, null=True)  # Field name made lowercase.
    add_02_empl = models.CharField(db_column='Add_02_Empl', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    add_02_datetime = models.DateTimeField(db_column='Add_02_DateTime', blank=True,
                                           null=True)  # Field name made lowercase.
    add_03_file = models.CharField(db_column='Add_03_File', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    add_03_date = models.DateField(db_column='Add_03_Date', blank=True, null=True)  # Field name made lowercase.
    add_03_empl = models.CharField(db_column='Add_03_Empl', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    add_03_datetime = models.DateTimeField(db_column='Add_03_DateTime', blank=True,
                                           null=True)  # Field name made lowercase.
    calcpaywork = models.CharField(db_column='CalcPayWork', max_length=500, blank=True,
                                   null=True)  # Field name made lowercase.
    numbserv = models.IntegerField(db_column='NumbServ')  # Field name made lowercase.
    usersdb = models.CharField(db_column='UsersDb', max_length=30)  # Field name made lowercase.
    compusers = models.CharField(db_column='CompUsers', max_length=30)  # Field name made lowercase.
    datetimech = models.DateTimeField(db_column='DateTimeCh')  # Field name made lowercase.
    nscreator = models.IntegerField(db_column='NSCreator')  # Field name made lowercase.
    idel = models.IntegerField(db_column='iDel')  # Field name made lowercase.
    aut_doc = models.CharField(max_length=30)
    ar_all_view = models.IntegerField()
    ar_all_edit = models.IntegerField()
    ar_gov_view = models.IntegerField()
    ar_gov_edit = models.IntegerField()
    ar_div_view = models.IntegerField()
    ar_div_edit = models.IntegerField()
    ar_aut_view = models.IntegerField()
    ar_aut_edit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cact719'


