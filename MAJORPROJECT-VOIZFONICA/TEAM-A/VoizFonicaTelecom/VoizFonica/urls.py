from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('add/',views.addadmin,name='addadmin'),
    path('add1/',views.addprepaid,name='addprepaid'),
    path('add2/',views.addpostpaid,name='addpostpaid'),
    path('add3/',views.adddongle,name='adddongle'),

    path('pre/',views.prepaidview,name='prepaidview'),
    path('post/',views.postpaidview,name='postpaidview'),
    path('don/',views.dongleview,name='dongleview'),
    path('lo/',views.adminlogout,name="adminlogout"),
    

    path('updatesearch1/',views.updatesearchapi1,name='updatesearchapi1'),
    path('updatesearch2/',views.updatesearchapi2,name='updatesearchapi2'),
    path('updatesearch3/',views.updatesearchapi3,name='updatesearchapi3'),
    path('update1/',views.preupdate,name='preupdate'),
    path('update2/',views.postupdate,name='postupdate'),
    path('update3/',views.dongleupdate,name='dongleupdate'),
    path('delete1/',views.prepaiddelete,name='prepaiddelete'),
    path('delete2/',views.postpaiddelete,name='postpaiddelete'),
    path('delete3/',views.dongledelete,name='dongledelete'),
    path('loginview/',views.loginview,name='loginview'),


    path('vie1/',views.previewss,name='previewss'),
    path('vie2/',views.postviewss,name='postviewss'),
    path('vie3/',views.dongleviewss,name='dongleviewss'),
    path('si1/',views.presearch,name='presearch'),
    path('si2/',views.postsearch,name='postsearch'),
    path('si3/',views.donglesearch,name='donglesearch'),
    
    path('update_action_api1/',views.update_data_read1,name='update_data_read1'),
    path('update_action_api2/',views.update_data_read2,name='update_data_read2'),
    path('update_action_api3/',views.update_data_read3,name='update_data_read3'),
    # path('deletesearch1/',views.deletesearchapi1,name='deletesearchapi1'),
    # path('deletesearch2/',views.deletesearchapi2,name='deletesearchapi2'),
    # path('deletesearch3/',views.deletesearchapi3,name='deletesearchapi3'),
    


    path('viewallpre/',views.prepaid_all,name='prepaid_all'),
    path('viewallpost/',views.postpaid_all,name='postpaid_all'),
    path('viewalldongle/',views.dongle_all,name='dongle_all'),
    path('updatepre/',views.updatesearchapi1,name='updatesearchapi1'),
    path('updatepost/',views.updatesearchapi2,name='updatesearchapi2'),
    path('updatedongle/',views.updatesearchapi3,name='updatesearchapi3'),
    
    path('login/',views.login_check,name='login_check'),

    path('admin/',views.adminPage),
    path('updatecust/',views.updateCustomers),

###############query#################################################################################
    path('updatequery/',views.updatesearchapiquery,name="updatesearchapiquery"),
    path('update_data_readquery/',views.update_data_readquery,name='update_data_readquery'),
    path('up/',views.updatequery,name='updatequery'),
    path('upa/<fetchid>',views.viewquerydetails,name='viewquerydetails'),
    path('viewquery/',views.viewquery,name='viewallqueries'),
    path('viewhtmlquery/',views.queryview,name='queryview'),

 ####################Customer##################################
    # path('lo/',views.Login),
    # path('index/',views.Index),
    # path('up/',views.Update),
    # path('logout/',views.signout),
    path('register/',views.customer),
    path('addcustomer/',views.addCustomer),
    path('view/<fetchid>',views.f_single),
    path('logout/',views.cuslogout),


    path('viewplans/',views.viewplans),
    # path('view/',views.viewCustomers,name='viewUsers'),
    # path('updatecustomer/',views.updateCustomers,name='updateUser'),
    path('update_data/',views.update_data,name='update_data'),
    path('update/',views.update_search,name="update_search"),
    path('deletecust/',views.delete_cust,name='delete_cust'),
    path('delete/',views.delete_data,name="delete_search"),
    # path('deletefromviews/<int:id>', views.deleteCustomer,name="deleteCustomer"), 
    path('viewall/',views.viewCust,name='viewCust'),
    path('viewCustomers/',views.viewCustomers,name='viewCustomers'),
    path('managecustomers/',views.manageCustomers,name='manageCustomers'),

    # path('viewall/',views.viewAll,name='viewAll'),
    
    path('login1/',views.login_checkcustomer,name='login_checkcustomer'),
    path('log/',views.loginviewcustomer,name='loginviewcustomer'),
    path('home/',views.homepage,name='homepage'),
    path('rsuc/',views.registersuccess,name='registersuccess'),
    path('services/',views.customerservices,name='customerservices'),
    path('faq/',views.customerfaq,name='customerfaq'),


    path('preplans/',views.viewpreplans,name='preplan_list'),
    path('prepaidplans/',views.viewprepaidplans,name='viewprepaidplans'),


    # path('postplan/',views.postplans),
    path('postplans/',views.viewpostplans,name='viewpostplans'),
    path('postpaidplans/',views.viewpostpaidplans,name='viewpostpaidplans'),
    path('try/',views.try1,name='try1'),
    path('donplans/',views.viewdongleplans,name='viewdongleplans'),
    # path('dplans/',views.viedongle,name='viedongle'),
    path('d/',views.viewdonplans,name='viewdonplans'),



##########################email###################################################
# path('send_mail_plain',views.SendPlainEmail,name='plain_email'),

# path('send_mail_plain_with_stored_file', views.send_mail_plain_with_stored_file, name='plain_email'),

# path('send_mail_plain_with_file', views.send_mail_plain_with_file, name='plain_email'),
    path('recharge/',views.prepaidinvoice,name='prepaidinvoice'),
    path('success/',views.successrec,name='successrec'),
    path('preinvoice/',views.addprepaidinvoice,name='addprepaidinvoice'),
    path('pdf/',views.venue_pdf,name='pdf'),

#######customerquery########################################################
    path('customerquery/',views.cusquery),
    path('queryupdate/',views.update_dataquery),
    path('queryFaq/',views.custf),
    path('addquery/',views.addquery),

    path('upload/',views.upload,name='upload'),
#############################################################################
    path('view1/<id>',views.prepaid_details,name="prepaid_details"),
    path('view2/<id>',views.postpaid_details,name="postpaid_details"),
    path('view3/<id>',views.dongle_details,name="dongle_details"),
    path('edit/',views.edit),
    path('dashservices/',views.services),
    path('ourservices/',views.ourservices),
    path('contact/',views.contact),
    path('about/',views.about),
    path('viewbill1/',views.viewbill),

#################################Bill#####################################################
    path('addusage/',views.addusagedata,name='addusagedata'),
    path('addata/',views.addata,name='addata'),
    ##################
    path('addbill/',views.addbilldata,name='addbilldata'),
    path('addbillhtml/',views.addbill,name='addbill'),
    ##################
    path('searchusage/',views.searchUsage,name='searchUsage'),#customer bill view
    path('searchadminusage/',views.searchadminUsage,name='searchadminusage'), #admin billview
   ###########################
   path('searchapi/',views.searchapi,name='searchapi'),
    path('searchapi2/',views.searchapi2,name='searchapi2'),
    #####################
    path('viewbill/',views.viewbillpost,name='viewbillpost'),
    path('billview/',views.billview,name='billview'),
    path('billpdf/<mobile>',views.billvenue_pdf,name='billvenue_pdf'),
    path('billheader/',views.billheader,name='billheader'),
    path("Raisequery/",views.Raisequery,name='Raisequery'),
    path("querysolution/",views.querysolution,name='querysolution'),
    path('querysolution/',views.viewquerysolution,name='viewquerysolution'),
    path('querysol/',views.searchapis,name='searchapis'),
    path('manageplans/',views.manage,name='manage'),



#############SEND MAIL#################
path('customeremail/',views.customeremail,name='customeremail'),
path('emailapi/',views.send_emailasfile,name='send_emailasfile'),




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
