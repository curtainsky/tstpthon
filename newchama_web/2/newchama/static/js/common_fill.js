
if ($.fn.popover) { $('.ui-popover').popover ({ container: 'body' }) }

try {
    jQuery('#expire_date').datepicker({format: 'yyyy-mm-dd'});
    jQuery('#lock_date').datepicker({format: 'yyyy-mm-dd'});
} catch(e){}

jQuery("input[name='is_list_company']").click(function() {
    if ($(this).val() == 1) {
        $("#ticker").attr("disabled", false);
    }
    else {
        $("#ticker").attr("disabled", true);
    }
});

$('input[data-type="number"]').iMask({
    type : 'number',
    decDigits : -1 ,
    decSymbol : '',
    sanity : function( val ){
        //return Math.min( 100000000000, Math.max(0, parseFloat( val.replace(/[^\.\d]/g, ''))));
        return Math.min( 999999999999, Math.max(0, parseFloat( val.replace(/[^\.\d]/g, ''))));
    }
});

jQuery("#country").change(function(){
    LoadProvinces('province',jQuery(this).val(),0);
});


jQuery("#is_audited").click(function() {
    if (jQuery(this).prop("checked")) {
        $("#financial_audit_company_name").attr("required", true);
        jQuery(".bigfour").show();
    }
    else {
        $("#financial_audit_company_name").attr("required", false);
        jQuery(".bigfour").hide();
    }
});

$(".s_rate_bak").keyup(function() {
    var total = 0;
    var index = $(".s_rate").index($(this));
    $(".s_rate").each(function(i) {
        if (index < i) {
            var result = 100 - parseFloat(total);
            if (result <= 0) {
                $(this).val("0");
            }
            else {
               if (isNaN(result)) result = 0;
                $(this).val(result);
            }
        }
        if (index == i) {
            var result = 100 - parseFloat(total) - $(this).val();
            if (result < 0) {
                $(this).val(100 - parseFloat(total));
            }
        }
        total += parseFloat($(this).val());
    });
});

jQuery('#target_company_industry_0').change(function() {
    var val = jQuery(this).val();
    var name = jQuery("#target_company_industry_0 option:selected").text();
    jQuery("#target_industry_id").val(val);
    jQuery("#target_industry_name").val(name);
    jQuery("#target_company_industry_1").parent().hide();
    jQuery("#target_company_industry_2").parent().hide();
    if (val == "0" || val == "") return;
    industrySelect("target_company_industry_1", val);
});

jQuery('#target_company_industry_1').change(function() {
    var val = jQuery(this).val();
    var name = jQuery("#target_company_industry_1 option:selected").text();
    jQuery("#target_industry_id").val(val);
    jQuery("#target_industry_name").val(name);
    jQuery("#target_company_industry_2").parent().hide();
    if (val == "0" || val == "") return;
    industrySelect("target_company_industry_2", val);
});

jQuery('#target_company_industry_2').change(function() {
    var val = jQuery(this).val();
    var name = jQuery("#target_company_industry_2 option:selected").text();
    jQuery("#target_industry_id").val(val);
    jQuery("#target_industry_name").val(name);
});

jQuery('#company_industry_0').change(function() {
    var val = jQuery(this).val();
    var name = jQuery("#company_industry_0 option:selected").text();
    jQuery("#industry_id").val(val);
    jQuery("#industry_name").val(name);
    jQuery("#company_industry_1").parent().hide();
    jQuery("#company_industry_2").parent().hide();
    if (val == "0" || val == "") return;
    industrySelect("company_industry_1", val);
});

jQuery('#company_industry_1').change(function() {
    var val = jQuery(this).val();
    var name = jQuery("#company_industry_1 option:selected").text();
    jQuery("#industry_id").val(val);
    jQuery("#industry_name").val(name);
    jQuery("#company_industry_2").parent().hide();
    if (val == "0" || val == "") return;
    industrySelect("company_industry_2", val);
});

$("#service_type").change(function() {
    var val = jQuery(this).val();
    if (val == 2) $(".project_stage").removeClass("hide_");
    else $(".project_stage").addClass("hide_");
});

jQuery('#company_industry_2').change(function() {
    var val = jQuery(this).val();
    var name = jQuery("#company_industry_2 option:selected").text();
    jQuery("#industry_id").val(val);
    jQuery("#industry_name").val(name);
});


$("#ticker" ).autocomplete({
  source: function( request, response ) {
    $.ajax({
      url: "/repository/get_listed_companies/"+request.term,
      dataType: "json",
      success: function( jsonResponse ) {
         var data = $(jsonResponse).map(function(id,item) {
          return {
            value: item.fields.stock_symbol,
            label: item.fields.stock_symbol + ":" + item.fields.short_name_en,
            id: item.pk
          };
        })
       response(data);
      }
    });
  },
  minLength: 2
});

jQuery("#target_company").autocomplete({
    source: function( request, response ) {
        $.ajax({
            url: "/repository/get_active_companies/"+request.term,
            dataType: "json",
            success: function( jsonResponse ) {
                var data = $(jsonResponse).map(function(id,item) {
                    return {
                        value: item.fields.name_cn,
                        label: item.fields.name_cn,
                        id: item.pk
                    }
                });
                response(data);
            }
        });
    },
    minLength: 2,
    select: function(event, data) {
        jQuery("#target_company_id").val(data.item.id);
    }
});

function addIndustry2() {
    var industry_id = jQuery("#target_industry_id").val();
    var industryName = jQuery("#target_industry_name").val();
    if (industry_id == "0" || industry_id == "") return;
    if (!isObjectExsit("target_industry_" + industry_id)) {
        var html = "<span id='target_industry_" + industry_id + "' class='alert alert-info preference_selected'><a href='###'>" + industryName + "</a>&nbsp;<a href='###' data-dismiss='alert' class='glyphicon glyphicon-remove'></a>" +
            "<input name='target_industries' type='hidden' value='" + industry_id + "'></span>";
        jQuery("#target_industry").append(html);
    }
}

function addCompany2() {
    var id = jQuery("#target_company_id").val();
    var name = jQuery("#target_company").val();
    if (id == "0" || id == "") return;
    if (!isCompanyExsit(id)) {
        $(".target_company_div").removeClass("hide_");
        //在id=target_company_ 加 2_ 是因为查询推荐机构是从listedcompany中查询的，为了在编辑状态下能正确删除，所以添加对应节点说明，否则同一个id因为可能从member_company,investment_company和listed_company中获取到重复的id
        var html = "<span id='target_company_1_" + id + "' class='alert alert-info preference_selected'><a href='###'>" + name + "</a>&nbsp;<a href='###' data-dismiss='alert' class='glyphicon glyphicon-remove'></a>" +
            "<input name='target_companies' type='hidden' value='" + id + "'></span>";
        jQuery("#target_compaies").append(html);
        jQuery("#target_company").val("");
        jQuery("#target_company_id").val("");
    }
}

function isCompanyExsit(val) {
    var bool = false;
    jQuery("input[name='target_companies']").each(function() {
        if (jQuery(this).val() == val) {
            bool = true;
            return false;
        }
    });
    return bool;
}

function addMember2() {
    var id = jQuery("#target_member_id").val();
    var name = jQuery("#target_member").val();
    if (id == "0" || id == "") return;
    if (!isObjectExsit("target_member_" + id)) {
        var html = "<span id='target_member_" + id + "' class='alert alert-info preference_selected'><a href='###'>" + name + "</a>&nbsp;<a href='###' data-dismiss='alert' class='glyphicon glyphicon-remove'></a>" +
            "<input name='target_members' type='hidden' value='" + id + "'></span>";
        jQuery("#target_members").append(html);
        jQuery("#target_member").val("");
        jQuery("#target_member_id").val("");
    }
}

function addKeyword2() {
    var name = jQuery("#key_keyword").val();
    if (name == "") return;
    if (!isObjectExsit("target_keyword_" + name)) {
        var html = "<span id='target_keyword_" + name + "' class='alert alert-info preference_selected'><a href='###'>" + name + "</a>&nbsp;<a href='###' data-dismiss='alert' class='glyphicon glyphicon-remove project_key_remove' ref='"+name+"'></a>" +
            "</span>";
        jQuery("#target_keywords").append(html);
        var val = jQuery("#project_keyword").val();
        if (val == "")
            val = name;
        else
            val += "," + name;
        jQuery("#project_keyword").val(val);
        jQuery("#key_keyword").val("")
    }
}

$(".panel-body").delegate(".project_key_remove", "click", function() {
    var val = $(this).parent().text().trim() + ",";
    var key = $("#project_keyword").val() + ",";
    key = key.replace(val, "");
    $("#project_keyword").val(key.substring(0, key.length - 1));
});

$(".panel-body").delegate(".glyphicon-remove", "click", function() {
    var len = $("#target_compaies .preference_selected").length;
    if (len <= 1) {
        $(".target_company_div").addClass("hide_");
    }
});

function isObjectExsit(id) {
    return (jQuery("#"+id).val()!=undefined);
}

$("#btn_add_attach").click(function() {
    var type = $("#attachment_type").val();
    if (type == "") {
        alert("请先选择您要上传的附件类型");
        return;
    }
    if (isAttachExsit(type)) {
        alert("该附件已存在");
        return;
    }
    var name = $("#attachment_type option:selected").text();
    var html = "<div class='form-group attach_sub' ref='" + name + "'><label class='col-md-3 control-label'>" + name + "</label>" +
                "<div class='col-md-6'><input type='hidden' name='upload_types' value='" + type + "'><input type='hidden' name='upload_type_names' value='" + name + "'><input type='file' name='upload_file_" + type + "' /></div></div>";
    $(".panel-footer").before(html);
});

$("#btn_remove_attach").click(function() {
//    if ($(".attach_sub").length <= 1) {
//        return;
//    }
    var txt = $(".attach_sub").last().attr("ref");

    if (confirm("您确定要删除 [ " + txt + " ] 的附件吗?")) {
        $(".attach_sub").last().remove();
    }
});

function isAttachExsit(type) {
    var bool = false;
    $("input[name='upload_types']").each(function() {
       if ($(this).val() == type) {
           bool = true;
           return false;
       }
    });
    return bool;
}

 $('input[data-type="percent"]').iMask({
     type : 'number',
     decDigits : -1 ,
     decSymbol : '',
     sanity : function( val ) {
        return Math.min( 100, Math.max(0, parseFloat( val.replace(/[^\.\d]/g, ''))));
     }
 });

 $('input[data-type="percentPlus"]').iMask({
    type      : 'fixed',
    mask      : '99999',
    stripMask : true
 });

jQuery("input[name='is_suitor']").click(function() {
    var val = jQuery(this).val();
    if (val == "1")
        jQuery(".suitor input").attr("disabled", false);
    else
        jQuery(".suitor input").attr("disabled", true);
});

jQuery("#btn_reset").click(function() {
    location.href = location.href;
});

jQuery('#project_keyword').tagsInput({
    'width':'auto',
    'height':'64px',
    'autocomplete_url': "/repository/getKeywords?inTags="+jQuery('#project_keyword').val()
});

jQuery('#project_keyword_en').tagsInput({
    'width':'auto',
    'height':'64px',
    'autocomplete_url': "/repository/getKeywords?inTags="+jQuery('#project_keyword_en').val()
});

jQuery('#project_keyword_admin').tagsInput({
    'width':'auto',
    'height':'64px',
    'autocomplete_url': "/repository/getKeywords?inTags="+jQuery('#project_keyword_admin').val()
});

$("#btn_save").click(function() {
    $("#submitStatus").val("pending");
    $(".alert-warning").remove();
    $("#btn_save").prop("disabled", true);
    endSave(function(bool) {
        if (bool) {
            var url = $("#listPage").val();
            if (url.indexOf("project") > 0)
                sync_recommend("/project/sync_recommend/");
            else
                sync_recommend("/demand/sync_recommend/");
            location.href=$("#listPage").val();
        }
        else if (!bool)
            $("#btn_save").prop("disabled", false);
    });
});

function sync_recommend(url) {
    var postUrl = url + $("#edit_id").val();
    $.ajax({url: postUrl});
    alert("操作成功，正在为您匹配最适合您的投资机构");
}

$("#btn_draft").click(function() {
    $("#submitStatus").val("draft");
    $(".alert-warning").remove();
    $("#btn_draft").prop("disabled", true);
    endSave(function(bool) {
        if (bool)
            location.href=$("#listPage").val();
        $("#btn_draft").prop("disabled", false);
    });
});

function endSave(fun_) {
	$("#formData").ajaxSubmit({
	    type: 'post',
	    dataType: 'json',
	    success: function(data) {
            if (data.result == "success") {
                $("#edit_id").val(data.id);
                fun_(true);
            }
            else {
                if (data.message == "typeError")
                    errorMessages("上传文件必须是doc|docx|pdf|ppt|pptx");
                else if (data.message == "tooBig")
                    errorMessages("文件大小不能大于20兆");
                else
                    errorMessages(data.message);
                location.href="#";
            }
            fun_(false);
	    },
        beforeSerialize:  function($form, options) {
            if( !$('#regionlevelthree').val() ) {
                $('#regionlevelthree').focus();
                fun_(false);
                return false;
            }
        }
	});
}

function  errorMessages(errorMsg) {
    var html = '<div class="alert alert-warning"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>'+ errorMsg +'</div>';
    $(".panel-body").prepend(html);
}