(window.odspNextWebpackJsonp=window.odspNextWebpackJsonp||[]).push([["139"],{"3619":function(e,t,n){"use strict";n.r(t);var r=n(0),i=n(1734),s=n(1491),o=n(1482),u=n(94),a=n(1485),f=n(48),l=n(1502),c=n(133);Object(c.n)([{rawString:".od-MalwareDetected-dialog-header{color:"},{theme:"errorText",defaultValue:"#a4262c"},{rawString:";font-size:21px;margin-bottom:15px}"}]);var h=n(1471),p=n(23),d=n(2804),v='<a href="https://go.microsoft.com/fwlink/?linkid=862871" target="_blank">'+d.e.malwareDetectedMessageLearnMore+"</a>",m=(function(e){Object(r.__extends)(t,e);function t(t){var n=e.call(this,t)||this;n.allowInfectedDownload=t.allowInfectedDownload;n.malwareDetectedIconUrl=window.require.toUrl("odsp-media/images/atp/malware_icon_168x168.svg");n.malwareDetectedMessageHeader=d.e.malwareDetectedDialogHeader;n.malwareDetectedMessage=p.format(d.e.malwareDetectedMessage,v);n.malwareDetectedAllowDownloadMessage=p.format(d.e.malwareDetectedAllowDownloadMessage,v);return n}return t})(h.t),g=n(1473).e({tagName:"od-malwareDetected",template:'<div class="od-MalwareDetected-dialog-content"><div class="od-MalwareDetected-dialog-header" data-bind="text:malwareDetectedMessageHeader"></div><div>\x3c!--ko if:allowInfectedDownload--\x3e<span data-bind="html:malwareDetectedAllowDownloadMessage"></span>\x3c!--/ko--\x3e\x3c!--ko ifnot:allowInfectedDownload--\x3e<span data-bind="html:malwareDetectedMessage"></span>\x3c!--/ko--\x3e</div></div>',viewModel:m}),y=n(635),b=n(1494),w=n(64),E=n(152),S=(function(e){Object(r.__extends)(t,e);function t(t){var n=e.call(this,t)||this;n.name="malwareDetected";n.dialogProvider=n.resources.consume(l.e);n._itemSelectionHelper=new(n.child(s.e))({overrideItem:t.item});n._responsiveUI=n.resources.consume(b.t);n._pageContext=n.resources.consume(w.h);n._navigation=n.resources.consume(E.e);n._itemUrlHelper=n.resources.consume(y.n);return n}t.prototype.onIsAvailable=function(){var e=this._itemSelectionHelper.firstItem();return e&&e.lifeCycleStatus&&e.lifeCycleStatus.isMalwareDetected};t.prototype.onExecute=function(e,t){this._getMalwareDetectedDialog();return u.n.wrap({resultType:f.e.Failure})};t.prototype._getMalwareDetectedDialog=function(){var e=this,t=this._pageContext.allowInfectedDownload,n=[];t&&n.push({name:a.e.Download,execute:function(){e._downloadInfectedItemViaClassic();return u.n.wrap(2)},isAvailable:this.observables.create(!0),icon:new o.e("Download"),isDefault:!0});n.push({name:t?a.e.declineInfectedDownload:a.e.ok,execute:function(){return u.n.wrap(2)},isAvailable:this.observables.create(!0),icon:new o.e("Cancel"),isDefault:!0});this.dialogProvider.requestDialog({component:{name:g.tagName,params:{allowInfectedDownload:t}},size:"Medium",actions:n,focusOnPrimaryAction:!0,isDismissable:!(this._responsiveUI.compareSize(this._responsiveUI.formFactorSize(),"Small")<=0)})};t.prototype._getItemClassicDownloadLink=function(){var e=this._itemSelectionHelper.firstItem();return this._itemUrlHelper.getItemUrlParts(e.key).fullItemUrl+"?avcmd=1"};t.prototype._downloadInfectedItemViaClassic=function(){var e=this._getItemClassicDownloadLink();e&&this._navigation.navigateTo({url:e,frameId:"_blank"})};return t})(i.e);t.default=S}}]);