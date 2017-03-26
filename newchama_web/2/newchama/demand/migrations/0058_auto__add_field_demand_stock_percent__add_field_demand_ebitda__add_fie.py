# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Demand.stock_percent'
        db.add_column('demand_demand', 'stock_percent',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Demand.ebitda'
        db.add_column('demand_demand', 'ebitda',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Demand.deal_size_enter'
        db.add_column('demand_demand', 'deal_size_enter',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Demand.expected_enterprice_value_enter'
        db.add_column('demand_demand', 'expected_enterprice_value_enter',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Demand.stock_percent'
        db.delete_column('demand_demand', 'stock_percent')

        # Deleting field 'Demand.ebitda'
        db.delete_column('demand_demand', 'ebitda')

        # Deleting field 'Demand.deal_size_enter'
        db.delete_column('demand_demand', 'deal_size_enter')

        # Deleting field 'Demand.expected_enterprice_value_enter'
        db.delete_column('demand_demand', 'expected_enterprice_value_enter')


    models = {
        u'adminuser.adminuser': {
            'Meta': {'object_name': 'AdminUser'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isactive': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'realname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'role': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['adminuser.Role']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'adminuser.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'permission': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'area.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.Province']"})
        },
        u'area.continent': {
            'Meta': {'object_name': 'Continent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'area.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.Continent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intel_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'area.province': {
            'Meta': {'object_name': 'Province'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demand.demand': {
            'Meta': {'object_name': 'Demand'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)'}),
            'audit_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'business_cn': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'business_en': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'company_cities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['area.City']", 'null': 'True', 'blank': 'True'}),
            'company_countries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['area.Country']", 'null': 'True', 'blank': 'True'}),
            'company_industries': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'demand_target_company_industries'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['industry.Industry']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'company_provinces': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['area.Province']", 'null': 'True', 'blank': 'True'}),
            'company_stock_symbol': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'company_symbol': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'currency_type_financial': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deal_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deal_size_enter': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'ebitda': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'employees_count_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expected_enterprice_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expected_enterprice_value_enter': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'expire_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'financial_audit_company_is_must_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financial_audit_company_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'financial_is_must_audit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financial_year': ('django.db.models.fields.IntegerField', [], {'default': '2015'}),
            'growth_three_year': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2'}),
            'has_attach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'income_enter': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'income_last_phase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'integrity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'integrity_en': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'intro_cn': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'intro_en': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'is_anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_list_company': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_recommend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_suitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'member_demand_publisher'", 'to': u"orm['member.Member']"}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_project_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_project_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'net_assets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pay_currency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pay_way': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'process': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profit_enter': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'profit_last_phase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'project_relation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'project_stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'registered_capital': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'remark_cn': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'remark_en': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'service_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stock_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'stock_structure_percentage_type_institutional': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stock_structure_percentage_type_management': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stock_structure_percentage_type_private': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'target_companies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'project_target_companies'", 'symmetrical': 'False', 'to': u"orm['member.Company']"}),
            'target_industries': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'demand_push_target_industries'", 'symmetrical': 'False', 'to': u"orm['industry.Industry']"}),
            'target_members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'demand_push_target_members'", 'symmetrical': 'False', 'to': u"orm['member.Member']"}),
            'total_assets': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'total_assets_last_phase': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_profit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'valid_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demand.demandattach': {
            'Meta': {'object_name': 'DemandAttach', 'db_table': "'demand_demandAttach'"},
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_attach'", 'to': u"orm['demand.Demand']"}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'file_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'file_type_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'demand.demandchecklog': {
            'Meta': {'object_name': 'DemandCheckLog', 'db_table': "'demand_check_log'"},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'adminuser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_check_log_adminuser'", 'to': u"orm['adminuser.AdminUser']"}),
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_check_log_demand'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'result': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'demand.demanddownloadlog': {
            'Meta': {'object_name': 'DemandDownloadLog', 'db_table': "'demand_download_log'"},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_download_log_demand'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_download_log_member'", 'to': u"orm['member.Member']"})
        },
        u'demand.demandindustry': {
            'Meta': {'object_name': 'DemandIndustry'},
            'cv1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cv2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cv3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_industries'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'demand.demandkeyword': {
            'Meta': {'object_name': 'DemandKeyword', 'db_table': "'demand_keyword'"},
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_keyword'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'})
        },
        u'demand.demandkeywordadmin': {
            'Meta': {'object_name': 'DemandKeywordAdmin', 'db_table': "'demand_keyword_Admin'"},
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_keyword_admin'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'})
        },
        u'demand.demandkeyworden': {
            'Meta': {'object_name': 'DemandKeywordEn', 'db_table': "'demand_keyword_en'"},
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_keyword_en'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'})
        },
        u'demand.demandothertargetcompany': {
            'Meta': {'object_name': 'DemandOtherTargetCompany', 'db_table': "'demand_other_target_company'"},
            'company_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_other_company'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'short_name_cn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'short_name_en': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'table_name': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'demand.demandprintlog': {
            'Meta': {'object_name': 'DemandPrintLog', 'db_table': "'demand_print_log'"},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_print_log_demand'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_print_log_member'", 'to': u"orm['member.Member']"})
        },
        u'demand.demandrecommendlog': {
            'Meta': {'object_name': 'DemandRecommendLog', 'db_table': "'demand_recommend_log'"},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_recommend_log_demand'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'demand.demandtargetprojectdetail': {
            'Meta': {'object_name': 'DemandTargetProjectDetail', 'db_table': "'demand_target_project_detail'"},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)'}),
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_detail'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_detail_member'", 'to': u"orm['member.Member']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_detail_project'", 'to': u"orm['project.Project']"}),
            'recommend_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'update_member': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'demand_detail_update_member'", 'null': 'True', 'to': u"orm['member.Member']"}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        u'demand.demandviewlog': {
            'Meta': {'object_name': 'DemandViewLog', 'db_table': "'demand_view_log'"},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'demand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_view_log_demand'", 'to': u"orm['demand.Demand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demand_view_log_member'", 'to': u"orm['member.Member']"})
        },
        u'industry.industry': {
            'Meta': {'object_name': 'Industry'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['industry.Industry']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'member.company': {
            'Meta': {'object_name': 'Company'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)'}),
            'address_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'capital_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.City']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.Country']", 'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'found_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['industry.Industry']", 'null': 'True', 'blank': 'True'}),
            'intro_cn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'intro_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'intro_file': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'investment_experience_cn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'investment_experience_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'memo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent_company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Company']", 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.Province']", 'null': 'True', 'blank': 'True'}),
            'short_name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'short_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'member.member': {
            'Meta': {'object_name': 'Member'},
            'activecode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'default.jpg'", 'max_length': '100', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Company']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'creator'", 'null': 'True', 'to': u"orm['adminuser.AdminUser']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'expire_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'focus_aspect': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['industry.Industry']", 'symmetrical': 'False'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_cn': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'intro_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'invite_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'invite_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Member']", 'null': 'True', 'blank': 'True'}),
            'last_login_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'login_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'mobile_intel': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owner'", 'null': 'True', 'to': u"orm['adminuser.AdminUser']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position_cn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'position_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'tel_intel': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)'}),
            'audit_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'audit_status_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'audit_status_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company_cities': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.City']", 'null': 'True', 'blank': 'True'}),
            'company_country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.Country']", 'null': 'True', 'blank': 'True'}),
            'company_industry': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'project_company_industry'", 'null': 'True', 'to': u"orm['industry.Industry']"}),
            'company_industry_intro_cn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'company_industry_intro_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'company_intro_cn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'company_intro_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'company_name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'company_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'company_province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['area.Province']", 'null': 'True', 'blank': 'True'}),
            'company_stock_exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['repository.StockExchange']", 'null': 'True', 'blank': 'True'}),
            'company_stock_symbol': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'company_symbol_cn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'company_symbol_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'currency_type_financial': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'currency_type_service': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cv1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cv2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cv3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deal_size': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ebitda': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'ebitda_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'ebitda_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'employees_count_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expected_enterprice_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'expire_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'features_cn': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'features_en': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'financial_audit_company_is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financial_audit_company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'financial_is_audit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financial_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'growth_three_year': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2'}),
            'has_attach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'income_last_phase': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'income_last_phase_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'income_last_phase_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'income_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'integrity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'integrity_en': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'intro_cn': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'intro_en': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'is_agent_project': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_follow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_list_company': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_recommend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_suitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lock_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'member_publisher'", 'to': u"orm['member.Member']"}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pay_currency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'price_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'process': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'profit_last_phase': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'profit_last_phase_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'profit_last_phase_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'profit_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'project_relation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'project_stage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'registered_capital': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'service_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stock_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'target_companies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['member.Company']", 'symmetrical': 'False'}),
            'target_industries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['industry.Industry']", 'symmetrical': 'False'}),
            'target_members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['member.Member']", 'symmetrical': 'False'}),
            'total_assets_last_phase': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'total_assets_last_phase_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'total_assets_last_phase_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'total_profit_last_phase': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'total_profit_last_phase_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'total_profit_last_phase_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 1, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'valid_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'repository.stockexchange': {
            'Meta': {'object_name': 'StockExchange'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'short_name_cn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'short_name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['demand']