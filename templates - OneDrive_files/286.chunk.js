(window.odspNextWebpackJsonp=window.odspNextWebpackJsonp||[]).push([["286"],{"1481":function(e,t,n){"use strict";n.d(t,"e",function(){return s});var r=n(0),i=n(389),s=(function(){function e(e,t){var n=this._pageContext=t.pageContext,s=t.tokenProvider,o=t.dataRequestorType,u=void 0===o?(function(e){Object(r.__extends)(t,e);function t(t){return e.call(this,t,{pageContext:n,tokenProvider:s})||this}return t})(i.t):o,a=e.dataSourceName,f=void 0===a?"DataSource":a;this.dataRequestor=new u({qosName:f})}e.prototype.getDataSourceName=function(){return this.dataSourceName};e.prototype.needsRequestDigest=function(e){return!0};e.prototype.getData=function(e,t,n,r,i,s,o,u,a,f,l,c,h){void 0===i&&(i="POST");var p=e(),d=r&&r(),v=this.needsRequestDigest(p);return this.dataRequestor.getData({url:p,parseResponse:t,qosName:n,additionalPostData:d,method:i,additionalHeaders:s,contentType:o,maxRetries:u,noRedirect:a,crossSiteCollectionCall:f,telemetryHandler:l,qosExtraData:c,needsRequestDigest:v,authToken:h})};return e})();t.t=s},"2978":function(e,t,n){"use strict";n.d(t,"e",function(){return r});function r(e){var t=e.serverRelativeItemUrl,n=e.dataRequestor,r=e.webApiUrl,i=e.duration,s=void 0===i?1:i,o=e.authToken,u=r;u=(u=u.methodWithAliases("GetFileByServerRelativePath",{DecodedUrl:t})).method("GetPreAuthorizedAccessUrl",s);return n.getData({url:u.toString(),method:"GET",authToken:o,qosName:"ItemDataSource.getDownloadUrl"}).then(function(e){return e.d.GetPreAuthorizedAccessUrl})}},"3646":function(e,t,n){"use strict";n.r(t);var r=n(0),i=n(1481),s=n(94),o=n(180),u=n(74),a=n(1332),f=n(281),l=n(136),c=n(2978),h=n(438),p=(function(e){Object(r.__extends)(t,e);function t(t){var n=e.call(this,{},{pageContext:t})||this;n._itemUrlHelper=new o.e({},{pageContext:t});n._apiUrlHelper=new a.e({},{pageContext:t,itemUrlHelper:n._itemUrlHelper});return n}t.prototype.downloadItems=function(e){var t=e.items[0];return this.getDownloadUrl(t,null,{downloadType:0}).then(function(e){window.location.href=e})};t.prototype.getDownloadUrl=function(e,t,n){var r=this;void 0===n&&(n={});var i=n.downloadType,o=void 0===i?0:i,a=this._itemUrlHelper.getItemUrlParts(e.key);if(1===o)return s.n.resolve(Object(h.e)(a.fullItemUrl));if(3===o){var p=void 0;p=e.video?24:1;var d=this._apiUrlHelper.build().webByItemUrl(a);return Object(c.e)({dataRequestor:this.dataRequestor,webApiUrl:d,duration:p,serverRelativeItemUrl:a.serverRelativeItemUrl})}if(2===o)return a.isCrossDomain&&n.authToken?this.dataRequestor.getData({url:this._apiUrlHelper.contextInfoUrl(a.fullItemUrl),method:"POST",qosName:"GetContextInfo",authToken:n.authToken}).then(function(e){var t=e.d.GetContextWebInformation.WebFullUrl,n=new f.t({webAbsoluteUrl:t}).build().segment("web").methodWithAliases("GetFileByServerRelativePath",{DecodedUrl:a.serverRelativeItemUrl}).segment("OpenBinaryStream");return s.n.resolve(n.toString())}):s.n.resolve(this.getBinaryStreamApiUrl(a).toString());var v=void 0;if(t||a.siteRelation===u.r.sameSite){var m=void 0;if(t){m=this._itemUrlHelper.getItemUrlParts(t.key).fullItemUrl}else m=this._pageContext.webAbsoluteUrl;v=s.n.resolve(m)}else v=this.dataRequestor.getData({url:this._apiUrlHelper.contextInfoUrl(a.fullItemUrl),method:"POST",qosName:"GetContextInfo"}).then(function(e){return e.d.GetContextWebInformation.WebFullUrl});return v.then(function(e){return e+"/"+r._pageContext.layoutsUrl+"/download.aspx?"+Object(l.e)({SourceUrl:a.serverRelativeItemUrl})})};t.prototype.getBinaryStreamApiUrl=function(e){var t=this._apiUrlHelper.build().webByItemUrl(e);t=(t=t.methodWithAliases("GetFileByServerRelativePath",{DecodedUrl:e.serverRelativeItemUrl})).segment("OpenBinaryStream");var n=this._pageContext.authToken;n&&(t=t.oDataParameter("access_token",n));return t};return t})(i.t),d=n(1497),v=n(152),m=n(17),g=n(487),y=n(1495),b=n(327),w=n(64),E=n(796),S=n(1760),x=n(635),T=n(129),N=n(439),C=n(60);n.d(t,"resourceKey",function(){return L});var k=(function(){function e(e,t){this._common=new p(t.pageContext);this._dataRequestor=new t.dataRequestorType({});this._graphDataSource=t.graphDataSource;this._itemParentHelper=t.itemParentHelper;this._navigation=t.navigation;this._itemUrlHelper=t.itemUrlHelper;this._identityDataSource=t.identityDataSource}e.prototype.getDownloadUrl=function(e,t){void 0===t&&(t={});var n=Object(d.r)(this._itemParentHelper.getFacetedAncestorOrSelf(e,"subsite"));return this._common.getDownloadUrl(Object(S.n)(e),Object(S.n)(n),t)};e.prototype.getItemContents=function(e){var t=this;return this.getDownloadRequestParameters(e).then(function(e){var n=e.headers,r=n&&n.Authorization,i=r&&r.slice(7);return t._dataRequestor.getData({url:e.url,method:"GET",noRedirect:!0,qosName:"ItemDataSource.getItemContents",responseType:"blob",needsRequestDigest:!1,authToken:i})})};e.prototype.getDownloadRequestParameters=function(e,t){var n=this,r=this._itemUrlHelper.getItemUrlParts(e.key),i=new T.e(r.normalizedItemUrl);return r.isCrossDomain?this._identityDataSource.getSharePointToken(i.authority).then(function(t){var r=t.accessToken;return n.getDownloadUrl(e,{downloadType:2,authToken:r}).then(function(e){return{url:e,headers:{Authorization:"bearer "+r}}})}):this.getDownloadUrl(e,{downloadType:2}).then(function(e){return{url:e,withCredentials:!0}})};e.prototype.downloadItems=function(e){var t=this,n=e.items[0];return(Object(E.isFeatureEnabled)(E.UseVroomDownload)?this._graphDataSource.getDownloadUrl(n,{useDirectEndpoint:!0}):this.getDownloadUrl(n,{downloadType:0})).then(function(e){t._navigation.navigateTo(e)})};e.prototype.isDownloadBlocked=function(e){return!C.e.hasPermission(e.permissions,C.e.openItems)};return e})(),L=(t.default=k,Object(m.s)("DownloadDataSource",k,{dataRequestorType:g.n,graphDataSource:b.b,itemParentHelper:y.e,navigation:v.e,pageContext:w.h,itemUrlHelper:x.n,identityDataSource:N.t}))}}]);