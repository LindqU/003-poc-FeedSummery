class RssFeed:
  @property
  def mock_feed_items(self):
    return "hogehoge"
  

[{'title': 'Announcing beta launch of Display & Video 360 API v3', 'link': 'http://ads-developers.googleblog.com/2023/10/announcing-beta-launch-of-display-video.html', 'summary': 'We’re pleased to announce that <a href="https://developers.google.com/display-video/api/reference/rest/v3">Display &amp; Video 360 API v3</a> is available in public beta starting today.<br /><br />\n\nv3 includes a number of new features and breaking changes. Here are some of the changes introduced in v3:\n<ul>\n  <li>You can now fully manage <a href="https://support.google.com/displayvideo/answer/2705812#lists">proximity location lists</a>, enabling you to use the <a href="https://developers.google.com/display-video/api/reference/rest/v3/advertisers.locationLists.assignedLocations#methods"><code>advertisers.locationLists.assignedLocations</code></a> service to create and delete locations assigned to <code>TARGETING_LOCATION_TYPE_PROXIMITY</code> <a href="https://developers.google.com/display-video/api/reference/rest/v3/advertisers.locationLists#LocationList"><code>LocationList</code></a> resources.</li>\n  <li>You can now more easily enable optimized targeting for your line items using the new boolean <a href="https://developers.google.com/display-video/api/reference/rest/v3/TargetingExpansionConfig#FIELDS.enable_optimized_targeting"><code>enableOptimizedTargeting</code></a> field, which replaces the <code>targetingExpansionLevel</code> field in the <a href="https://developers.google.com/display-video/api/reference/rest/v3/TargetingExpansionConfig"><code>TargetingExpansionConfig</code></a> object.</li>\n  <li>The <a href="https://developers.google.com/display-video/api/reference/rest/v3/advertisers#Advertiser.FIELDS.billing_config"><code>billingConfig</code></a> field is now required in the <a href="https://developers.google.com/display-video/api/reference/rest/v3/advertisers#Advertiser"><code>Advertiser</code></a> resource and must be included when making <a href="https://developers.google.com/display-video/api/reference/rest/v3/advertisers/create"><code>advertisers.create</code></a> requests. To help with this, a new <a href="https://developers.google.com/display-video/api/reference/rest/v3/partners#Partner.FIELDS.billing_config"><code>billingConfig</code></a> field has been added to the <a href="https://developers.google.com/display-video/api/reference/rest/v3/partners#Partner"><code>Partner</code></a> resource to surface the billing information for the parent partner.</li>\n  <li><code>YoutubeAdGroup</code> and <code>YoutubeAdGroupAd</code> resources have been renamed to <a href="https://developers.google.com/display-video/api/reference/rest/v3/advertisers.adGroups#AdGroup"><code>AdGroup</code></a> and <a href="https://developers.google.com/display-video/api/reference/rest/v3/advertisers.adGroupAds#AdGroupAd"><code>AdGroupAd</code></a>.</li>\n</ul>\n\nMore detailed information about this release can be found in our <a href="https://developers.google.com/display-video/api/release-notes#october_2_2023">release notes</a>. Follow the steps in our <a href="https://developers.google.com/display-video/api/v3-migration-guide">migration guide</a> to migrate from v2 to v3. Be aware that breaking changes may be made to v3 while in beta and will be listed in the <a href="https://developers.google.com/display-video/api/release-notes">Display &amp; Video 360 API release notes</a>.<br /><br />\n\nIf you run into issues or need help with these new features or samples, please contact us using our <a href="https://support.google.com/displayvideo/contact/nghelp_contact_form">support contact form</a>.<br />\n\n<span class="byline-author"><img height="40" src="https://lh5.googleusercontent.com/ul6Bu6os82XfScd3uPkxcr4wuYHeOjBXB0TsB7mFIO-63RW7I-ciH9SZVTiRUk0NOGUg_8oit2oD7cr9HTrH8gol_Y6p8mqEeEWTQB24GyiZTGwpB-BFvji9n9goOPHz19mSYqtr" style="border: none; vertical-align: middle;" width="40" /> - Trevor Mulchay, Display &amp; Video 360 API Team</span>'}, {'title': 'Changes in dynamic ad targets reporting', 'link': 'http://ads-developers.googleblog.com/2023/09/changes-in-dynamic-ad-targets-reporting.html', 'summary': '<p>\nStarting on September 20, 2023, we’ve started rolling out a backend improvement on Google Ads dynamic ad targets reporting to include criteria that were removed and then added back as negative.\n</p>\n<p>\nBefore this change, report queries for web page criteria (that is, queries against the <code><a href="https://developers.google.com/google-ads/api/reference/rpc/latest/WebpageView">webpage_view</a></code> resource) requesting historical data did not include criteria that were removed and then added back as negative.\n\n<p>\nThis resulted in unexpected values in reports for the time frame when these criteria were accruing metrics (that is, when they were targeted and had <code>negative = false</code>), because the metrics they accrued in this time period were not returned in report query results.\n</p>\n<p>\nThe change only affects cases where a positive criterion was removed and added back as negative: all other criteria will return the same values they did before this change.\n</p>\n<p>\nAfter this change is released, criteria metrics will take into account removed criteria and criteria that were re-added as negative.\n</p>\n<p>\n<strong>Required actions</strong>\n</p>\n<p>\nYou don’t need to change anything in your GAQL queries; however, be aware that you may notice differences in criteria reporting after this change due to the correct values being reported.\n</p>\n<p>\nIf you have any questions or concerns, please don\'t hesitate to contact us via the <a href="https://groups.google.com/g/google-content-api-for-shopping">forum</a>.\n</p>\n\n\n<span class="byline-author"><img height="40" src="https://lh3.googleusercontent.com/a/AAcHTteMf_IXDYsJGIPAdLCefNLvUvK73hQtgnAZCJciyzpbfg=s83-c-mo" style="vertical-align: middle; border: none;" width="40" />&nbsp;-&nbsp;Mattia Tommasone, Google Ads API Team</span>'}, {'title': 'Google Ads Shopping Campaign Enhanced CPC Deprecation', 'link': 'http://ads-developers.googleblog.com/2023/09/google-ads-shopping-campaign-enhanced.html', 'summary': '<p>\nStarting in <strong>early October 2023</strong>, any Shopping campaigns using Enhanced cost-per-click (eCPC) will behave as if they are using Manual cost-per-click (CPC) bidding. \n</p>\n<p>\nEnhanced CPC was the first Smart Bidding strategy launched by Google over 10 years ago. It has been replaced by more advanced bidding strategies such as Target ROAS and Maximize conversion value, as well as fully automated campaigns like Performance Max.\n</p>\n<p>\n<strong>What happens if I change nothing?</strong>\n</p>\n<p>\nIf you choose to not make changes to your campaign by October 2023, it will operate as if it\'s using <a href="https://support.google.com/google-ads/answer/2464960">Manual CPC bidding</a>. All your existing campaigns using eCPC will continue serving using the manual bids that you set. If you set <code><a href="https://developers.google.com/google-ads/api/reference/rpc/v12/ManualCpc?hl=en#enhanced_cpc_enabled">ManualCpc.enhanced_cpc_enabled</a></code> to <code>true</code> in a Shopping campaign, the API ignores the setting and the campaign will only use Manual CPC bidding.\n\n<p>\n<strong>What should I change?</strong>\n</p>\n<p>\nIf you want to continue to use Manual CPC, remove any code that sets <code><a href="https://developers.google.com/google-ads/api/reference/rpc/v12/ManualCpc?hl=en#enhanced_cpc_enabled">ManualCpc.enhanced_cpc_enabled</a></code> to <code>true</code> for Shopping campaigns. We recommend these alternatives to Manual CPC:\n<ul>\n\n<li><a href="https://developers.google.com/google-ads/api/docs/shopping-ads/create-campaign#portfolio_bid_strategy">Target ROAS</a>\n<li>Our newest fully automated solution: <a href="https://developers.google.com/google-ads/api/docs/performance-max/getting-started">Performance Max campaigns</a></li></ul>\n\n<p>\n<strong>Where can I get support?</strong>\n</p>\n<p>\nIf you have questions, please reach out to us on the <a href="https://groups.google.com/forum/#!forum/adwords-api">forum</a> or at <a href="mailto:googleadsapi-support@google.com">googleadsapi-support@google.com</a>.\n</p>\n\n\n<span class="byline-author"><img height="40" src="https://lh6.googleusercontent.com/xc1BstqIO3rHCZTBaUVL-76euEtxewSqrhSqAgDA5IhL4CaYVYQywU1xeL3l7lwbL640tKrUIT2YsdYA9jAenuipiWbDPFpGKAL7XDRMhVDKRnF5aedoRE2NHFTHZkHtoLYNA1QdM-mLDo1mGNMB_8vduNcODY1_DE-9ER1JFov8HRQhoc8j6gWrx3A7mwM0bMhfi3LN3HcuKf1fwgVoWcSqjyq0WZVkwpjz" style="vertical-align: middle; border: none;" width="40" /> Nadine Wang, Google Ads API Team'}, {'title': 'Google Ads API support for importing and editing conversions from Google Analytics', 'link': 'http://ads-developers.googleblog.com/2023/09/google-ads-api-support-for-importing.html', 'summary': '<strong>What\'s changing</strong><br />\nStarting <strong>October 9, 2023</strong>, the Google Ads API will allow the following types of mutate operations for a <a href="https://developers.google.com/google-ads/api/reference/rpc/latest/ConversionAction">ConversionAction</a> imported from a Google Analytics 4 (GA4) property:\n<ol>\n  <li>An <code>update</code> that modifies <code>status</code>, <code>primary_for_goal</code>, <code>category</code>, <code>name</code>, or <code>value_settings</code>.</li>\n  <li>A <code>remove</code> that removes the conversion action.</li>\n</ol>\n\n<strong>Why this is important</strong><br />\nFor many Google Ads users, the conversions they import from Google Analytics are a critical component of bidding and reporting. Until now, you could use the Google Analytics Admin API to <a href="https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1beta/properties.googleAdsLinks/create">create a link</a> between your Google Analytics and Ads accounts, but you could not use the Google Ads API to complete the following remaining steps in the linking process:\n<ul>\n  <li>Importing each conversion from your GA4 property into your Google Ads account by modifying its <code>status</code> field from <code>HIDDEN</code> to <code>ENABLED</code>.</li>\n  <li>Configuring the <code>primary_for_goal</code> and <code>category</code> fields of each imported conversion to <a href="https://developers.google.com/google-ads/api/docs/conversions/goals/overview#conversion_action_settings">indicate how it should impact Google Ads bidding and reports</a>.</li>\n</ul>\n\nWith this change, the Google Ads API supports both of these steps and provides a complete API-based solution for linking your Google Analytics 4 property to your Google Ads account.<br /><br />\n\nIn addition to the attributes needed for proper configuration of <a href="https://developers.google.com/google-ads/api/docs/conversions/goals/overview">conversion goals</a>, you can now modify the following attributes of an imported GA4 <code>ConversionAction</code>:\n<ul>\n  <li><code>name</code></li>\n  <li><code>value_settings</code></li>\n</ul>\n\nRequests that attempt to modify any other attributes of an imported GA4 <code>ConversionAction</code> will continue to fail, as will requests that attempt to <code>remove</code> or <code>update</code> a <code>ConversionAction</code> imported from a Universal Analytics (UA) property.<br /><br />\n\n<strong>What you should do</strong><br />\nModify any code in your integration that depends on the Google Ads API rejecting a <a href="https://developers.google.com/google-ads/api/reference/rpc/latest/ConversionActionOperation"><code>ConversionActionOperation</code></a> with a <a href="https://developers.google.com/google-ads/api/reference/rpc/latest/MutateErrorEnum.MutateError#mutate_not_allowed"><code>MUTATE_NOT_ALLOWED</code></a> error if it attempts to <code>update</code> or <code>remove</code> an imported GA4 conversion. For example, if your integration relies on this behavior to detect if a conversion action is an imported GA4 conversion, modify it to instead check if the <a href="https://developers.google.com/google-ads/api/reference/rpc/latest/ConversionAction#type"><code>type</code></a> of the <code>ConversionAction</code> is either <code>GOOGLE_ANALYTICS_4_CUSTOM</code> or <code>GOOGLE_ANALYTICS_4_PURCHASE</code>.<br /><br />\n\nIn addition, if you currently complete the process of linking Google Analytics to Google Ads accounts using the UI, consider whether switching to an API-based solution is appropriate for your use case.<br /><br />\n\n<strong>How to get help</strong><br />\nIf you have any questions or need help, check out the Google Ads API <a href="https://developers.google.com/google-ads/api/support">support page</a> for options.<br />\n\n<span class="byline-author"><img height="40" src="https://lh5.googleusercontent.com/gbKcZtq3ZgxNsqeYRr1IwhfTwaDLoL_LffmZQp33VGeiPgZOAivPbSeBgyxlnIHw3aVxrjazymrwKflbXTozotvw99A9JdkN_xmSL86tCNSm3dFIWTZ5e8Y2lu9nkAP7f-M1C7XI_I3NI2CFnRPK_uI" style="vertical-align: middle; border: none;" width="40" /> - Josh Radcliff, Google Analytics and Google Ads API Team</span>'}, {'title': 'Buy on Google For Search and Shopping Deprecation', 'link': 'http://ads-developers.googleblog.com/2023/09/buy-on-google-for-search-and-shopping.html', 'summary': '<p>\n<strong>Buy on Google for Search and Shopping will no longer be available starting September 26, 2023</strong>. All Merchant and Consumer support will end for Buy on Google on Search on November 25, 2023. <strong>The only exception is that the <code>orders.get</code> and <code>orders.list</code> methods will remain available for Search and Shopping until October 30, 2024, so that merchants can download their historical order data. </strong>\n\n<p>\nSee below for the specific timeline of when Buy on Google methods will no longer be available for the Search and Shopping program.\n</p>\n<p>\n<strong>June 28, 2023</strong> onwards: \n</p><ul>\n\n<li><code><a href="https://developers.google.com/shopping-content/reference/rest/v2.1/buyongoogleprograms/requestreview">buyongoogleprograms.requestreview</a></code>\n<li><code><a href="https://developers.google.com/shopping-content/reference/rest/v2.1/buyongoogleprograms/onboard">buyongoogleprograms.onboard</a></code> \n<li><code><a href="https://developers.google.com/shopping-content/reference/rest/v2.1/buyongoogleprograms/activate">buyongoogleprograms.activate</a></code> \n<li><code><a href="https://developers.google.com/shopping-content/reference/rest/v2.1/buyongoogleprograms/pause">buyongoogleprograms.pause</a></code> </li></ul>\n\n<p>\n<strong>September 30, 2023</strong>: \n</p><ul>\n\n<li><code><a href="https://developers.google.com/shopping-content/reference/rest/v2.1/buyongoogleprograms/get">buyongoogleprograms.get</a></code>\n<li><code><a href="https://developers.google.com/shopping-content/reference/rest/v2.1/buyongoogleprograms/patch">buyongoogleprograms.patch</a></code></li></ul>\n\n<p>\n<strong>October 31, 2023</strong>: \n</p>\n<p>\nAll the <a href="https://developers.google.com/shopping-content/reference/rest/v2.1/orders">orders</a> related resources (<code>orders</code>, <code>orderinvoices</code>, <code>orderreports</code>, <code>orderreturns,</code> <code>ordertrackingsignals</code>) and all their underlying methods. The only exception is that the <code>orders.get</code> and <code>orders.list</code> methods will remain available for Search and Shopping until October 30, 2024, so that merchants can download their historical order data.\n</p>\n<p>\nIf you are currently using the Buy on Google endpoints for Search and Shopping via the Content API, you will need to stop using these services for Search and Shopping before the dates listed above, as your requests will start to fail after that date. \n</p>\n<p>\nIf you have any questions or concerns, please don\'t hesitate to contact us via the <a href="https://groups.google.com/g/google-content-api-for-shopping">forum</a>.\n</p>\n\n<span class="byline-author"><img height="40" src="https://lh6.googleusercontent.com/3UR5v4kdd7GrfXL7qxf9q5dUhvFCuGpErSk9b_VLFBrxtt2a8nNB4ka6wnxAjf_cESedQlAsF96iW-aNPGDANC2e0PMddceUlVVty7QfxD9qtapM1fRdGnU3qhDOEEQgXuJoQ3qaGumt7JfWD4wEcLsY" style="vertical-align: middle; border: none;" width="40" /> Benji Rothman, Content API for Shopping Team</span>'}, {'title': 'Performance Max: create listing groups using batch processing', 'link': 'http://ads-developers.googleblog.com/2023/09/performance-max-create-listing-groups.html', 'summary': '<h4>What’s New</h4>\n\n\n<p>\nStarting on October 4, 2023, <code><a href="https://developers.google.com/google-ads/api/reference/rpc/latest/AssetGroupListingGroupFilter">AssetGroupListingGroupFilters</a></code> can be created asynchronously using batch processing with the Google Ads API. If you use <code><a href="https://developers.google.com/google-ads/api/reference/rpc/latest/BatchJobService">BatchJobService</a></code> to create <code>AssetGroupListingGroupFilter</code> entities and other <a href="https://developers.devsite.corp.google.com/google-ads/api/docs/performance-max/overview">Performance Max resources</a> in a single request, errors in the listing group <a href="https://developers.google.com/google-ads/api/docs/performance-max/listing-groups">tree creation</a> will not block the creation of the remaining entities. However, the operations to create a listing group tree will still be atomic. This means that if any operation related to the creation of a listing group tree returns an error, all operations related to that listing group tree will also fail, save a few caveats, which are detailed in this <a href="https://developers.google.com/google-ads/api/docs/batch-processing/listing-groups">Jobs & listing group filters guide</a>.\n\n<p>\nThis update does not change the behavior of any existing batch jobs that do not include operations that create listing group filters.\n</p>\n<h4>\nPrevious Behavior\n</h4>\n<p>\nPrior to October 4, 2023, <code>AssetGroupListingGroupFilters</code> could only be created synchronously using the <code><a href="https://developers.google.com/google-ads/api/reference/rpc/v14/GoogleAdsService#mutate">GoogleAdsService.Mutate</a></code> or <code><a href="https://developers.google.com/google-ads/api/reference/rpc/v14/AssetGroupListingGroupFilterService#mutateassetgrouplistinggroupfilters">AssetGroupListingGroupFilterService.MutateAssetGroupListingGroupFilters</a></code> method. Requests using the <code>GoogleAdsService.Mutate</code> method are always atomic when they contain <code>AssetGroupListingGroupFilterOperation</code> operations. This is because <code>partial_failure</code> is not supported for these operations, which means that an error in listing group tree creation would block all other operations in the request. If you tried creating <code>AssetGroupListingGroupFilter</code> entities prior to October 4, 2023 using batch processing, you would receive a <code>MutateError.OPERATION_DOES_NOT_SUPPORT_PARTIAL_FAILURE</code> error.\n\n<h4>Change Rationale</h4>\n\n\n<p>\n<a href="https://developers.google.com/google-ads/api/docs/batch-processing/overview">Batch processing</a> is a powerful feature in the Google Ads API that allows you to dispatch a set of operations, which may be interdependent, to multiple services without synchronously waiting for the operations to complete. We have made batch processing available for <code>AssetGroupListingGroupFilters</code> in response to your <a href="https://developers.google.com/google-ads/api/docs/performance-max/feedback">feedback</a> to provide another option for creating listing group trees asynchronously and without blocking other operations in the same request.\n</p>\n<h4>Implementation Details</h4>\n\n\n<p>\nIn order to add an <code>AssetGroupListingGroupFilter</code> using a batch job:\n</p><ol>\n\n<li>Create a <code>MutateOperation</code> containing an <code>AssetGroupListingGroupFilterOperation</code>. This is no different than <a href="https://developers.google.com/google-ads/api/docs/performance-max/listing-groups#code_example">creating a MutateOperation using the GoogleAdsService.Mutate service</a>.\n<li>Add the <code>MutateOperation</code> to the batch job <a href="https://developers.google.com/google-ads/api/docs/batch-processing/flow#addoperations">as you would with any other type of operation</a>.</li></ol>\n\n<p>\nThe example below demonstrates the process of adding a single <code>AssetGroupListingGroupFilter</code> to an existing batch job. See the <a href="https://developers.google.com/google-ads/api/docs/performance-max/listing-groups">Creating Shopping Listing Groups guide</a> to learn more about creating product partition trees using <code>AssetGroupListingGroupFilter</code> entities.\n</p>\n\n<pre class="prettyprint lang-java">\n// Constructs the AssetGroupListingGroupFilter.\nAssetGroupListingGroupFilter listingGroupFilter =\n     AssetGroupListingGroupFilter.newBuilder()\n         .setAssetGroup(assetGroupResourceName)\n         .setType(ListingGroupFilterType.UNIT_INCLUDED)\n         .setVertical(ListingGroupFilterVertical.SHOPPING)\n         .build();\n\n// Constructs the operation to create the AssetGroupListingGroupFilter.\nMutateOperation operation = MutateOperation.newBuilder()\n     .setAssetGroupListingGroupFilterOperation(\n           AssetGroupListingGroupFilterOperation\n      .newBuilder()\n      .setCreate(listingGroupFilter))\n      .build();\n\n// Sends a request to add the operation to the batch job.\nAddBatchJobOperationsResponse response =\n    batchJobServiceClient.addBatchJobOperations(\n        AddBatchJobOperationsRequest.newBuilder()\n            .setResourceName(batchJobResourceName)\n            .addMutateOperations(operation)\n            .build());\n</pre>\n\n<p>\nThe following resources contain additional information to help you with your integration:\n</p><ul>\n\n<li><a href="https://developers.google.com/google-ads/api/docs/batch-processing/listing-groups">Jobs &amp; listing group filters guide</a>\n<li><a href="https://developers.google.com/google-ads/api/docs/performance-max/listing-groups">Listing groups guide</a>\n<li><a href="https://developers.google.com/google-ads/api/docs/batch-processing/overview">Batch processing guide</a></li></ul>\n\n<h4>Improving Performance Max integrations Blog Series</h4>\n\n\n<p>\nThis article is part of a series that discusses new and upcoming features that you have been asking for. We’ll cover what’s new and how it differs from the current implementation approach.\n</p>\n<p>\nKeep an eye out for further updates and improvements on our <a href="http://feeds.feedburner.com/ads-developers.googleblog.com">developer blog</a>, continue providing <a href="https://developers.google.com/google-ads/api/docs/performance-max/feedback">feedback on Performance Max</a> integrations with the Google Ads API, and as always, <a href="https://developers.google.com/google-ads/api/support">contact our team</a> if you need support.\n</p>\n\n\n<span class="byline-author"><img height="40" src="https://lh3.googleusercontent.com/a-/AOh14GiOcLXyMYphwRh10nyuK_-RpxNBRiDcaag6Z73p=s600-p-rwa" style="border: none; vertical-align: middle;" width="40" /> - Devin Chasanoff, on behalf of the Google Ads API Team</span>'}, {'title': 'Planned Content API maintenance from 15:00 UTC  to 17:00 UTC on September 28, 2023', 'link': 'http://ads-developers.googleblog.com/2023/09/planned-content-api-maintenance-from.html', 'summary': '<strong>The Content API for Shopping will undergo planned maintenance on September 28, 2023, from 15:00 to 17:00 UTC.</strong><br /><br />\n\nDuring this time, you will not be able to make any changes to your account such as updates to users, business information, feeds, shipping details, or linking your Google Ads accounts.<br /><br />\n\nYou can still upload products to your existing feeds or data sources and run ads as usual.<br /><br />\n\nNote that the Google Ads API is also affected by this outage, as you will not be able to link MC accounts and Google Ads accounts together via the Google Ads API during this time period.<br /><br />\n\nIf you have any questions or concerns, please don\'t hesitate to contact us via the <a href="https://groups.google.com/g/google-content-api-for-shopping">forum</a>.<br />\n\n<span class="byline-author"><img height="40" src="https://lh6.googleusercontent.com/3UR5v4kdd7GrfXL7qxf9q5dUhvFCuGpErSk9b_VLFBrxtt2a8nNB4ka6wnxAjf_cESedQlAsF96iW-aNPGDANC2e0PMddceUlVVty7QfxD9qtapM1fRdGnU3qhDOEEQgXuJoQ3qaGumt7JfWD4wEcLsY" style="vertical-align: middle; border: none;" width="40" /> Benji Rothman, Content API for Shopping Team</span>'}]