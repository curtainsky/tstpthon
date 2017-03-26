# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RecommondScore'
        db.delete_table('recommond_score')

        # Adding model 'RecommondItem'
        db.create_table('recommond_score', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Company'])),
            ('is_man', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_star', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_user', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_delete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('target_reason', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('add_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 27, 0, 0))),
            ('man_add_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 27, 0, 0))),
            ('sum_project_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sum_company_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_industry_keyword', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_industry_in_industry', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_industry_invest_industry_one', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_industry_invest_industry_two', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_deal_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_deal_size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_currency', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_finance_revenue', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_finance_growth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_finance_net_income', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_finance_ebitda', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_local', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_industry_keyword', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_industry_in_industry', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_industry_invest_industry_one', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_industry_invest_industry_two', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_deal_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_deal_size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_currency', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_finance_revenue', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_finance_growth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_finance_net_income', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_finance_ebitda', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_local', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 27, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'recommond', ['RecommondItem'])


    def backwards(self, orm):
        # Adding model 'RecommondScore'
        db.create_table('recommond_score', (
            ('sum_project_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_local', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_industry_invest_industry_two', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_finance_growth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_finance_net_income', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_deal_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_finance_growth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_finance_ebitda', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_industry_keyword', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_finance_revenue', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_score_currency', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_industry_invest_industry_one', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_deal_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sum_company_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_currency', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_deal_size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 25, 0, 0), auto_now=True, blank=True)),
            ('project_score_finance_revenue', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project_score_industry_in_industry', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Company'])),
            ('company_score_industry_invest_industry_two', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_finance_net_income', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_local', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_industry_keyword', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_finance_ebitda', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_deal_size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('company_score_industry_in_industry', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('company_score_industry_invest_industry_one', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'recommond', ['RecommondScore'])

        # Deleting model 'RecommondItem'
        db.delete_table('recommond_score')


    models = {
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
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 27, 0, 0)'}),
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
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 27, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'member.member': {
            'Meta': {'object_name': 'Member'},
            'activecode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'default.jpg'", 'max_length': '100', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Company']"}),
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
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
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
            'intro_cn': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'intro_en': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'is_agent_project': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_follow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_list_company': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_suitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lock_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'member_publisher'", 'to': u"orm['member.Member']"}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price_max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'price_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
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
            'update_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'valid_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'recommond.recommonditem': {
            'Meta': {'object_name': 'RecommondItem', 'db_table': "'recommond_score'"},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 27, 0, 0)'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Company']"}),
            'company_score_currency': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_deal_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_deal_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_finance_ebitda': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_finance_growth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_finance_net_income': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_finance_revenue': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_industry_in_industry': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_industry_invest_industry_one': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_industry_invest_industry_two': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_industry_keyword': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'company_score_local': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'has_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_man': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_star': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'man_add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 27, 0, 0)'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"}),
            'project_score_currency': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_deal_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_deal_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_finance_ebitda': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_finance_growth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_finance_net_income': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_finance_revenue': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_industry_in_industry': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_industry_invest_industry_one': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_industry_invest_industry_two': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_industry_keyword': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_score_local': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sum_company_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sum_project_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'target_reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 27, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
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

    complete_apps = ['recommond']