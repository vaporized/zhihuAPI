.. _action:

Actions
====================

This section lists APIs that performs actions with POST, PUT or DELETE. Actions are done with the current account.
Assuming you have created an instance:

.. code:: python

    from zhihuAPI.account import ZhihuAccount
    machine = ZhihuAccount('path/to/cookie.json')


Send Message (发送私信)
------------------------------
You need to pass additional information as follows:

:code:`content` is the content of the message.

:code:`receiver_hash` must be the ID of the target user, not url token.

.. code:: python

    machine.action('Me','SendMessage', '', _data={'content':..., 'receiver_hash':...})

Set Gender (设置性别)
------------------------------
You need to pass additional information as follows:

:code:`gender` is an integer. 0 for female, 1 for male, and -1 for not set.

.. code:: python

    machine.action('Me','SetGender', '', _data={'gender':...})

Set Headline (设置一句话介绍)
--------------------------------
You need to pass additional information as follows:

:code:`headline` is a string containing the introduction.

.. code:: python

    machine.action('Me','SetHeadline', '', _data={'headline':...})

Set Locations (设置居住地)
------------------------------
You need to pass additional information as follows:

:code:`locations` is a list of strings, for example, :code:`['province_name', 'city_name']`

.. code:: python

    machine.action('Me','SetLocations', '', _data={'locations':...})

Set Business (设置从事行业)
------------------------------
You need to pass additional information as follows:

:code:`business` is a string, and it must be from the available options in the list, otherwise it will
fail silently. Please refer to Zhihu for the complete list.

.. code:: python

    machine.action('Me','SetBusiness', '', _data={'business':...})

Set Employments (设置职业经历)
----------------------------------
You need to pass additional information as follows:

:code:`employments` is a list of dictionaries. :code:`[{'job':'job_name', 'company':'company_name'},...]`

.. code:: python

    machine.action('Me','SetEmployments', '', _data={'employments':...})

Set Educations (设置教育经历)
---------------------------------
You need to pass additional information as follows:

:code:`educations` is a list of dictionaries. :code:`[{'major':'major_name', 'school':'school_name'}]`

.. code:: python

    machine.action('Me','SetEducations', '', _data={'educations':...})

Set Description (设置个人简介)
---------------------------------
You need to pass additional information as follows:

:code:`description` is a string. The content should be wrapped with :code:`<p>xxxxx</p>`.

.. code:: python

    machine.action('Me','SetDescription', '', _data={'description':...})

Add Question (提问)
------------------------------
You need to pass additional information as follows:

:code:`title` is a string containing the title.

:code:`topic_url_tokens` is a list of topic IDs.

:code:`detail` is a string containing the description.

:code:`is_anonymous` is a boolean.

.. code:: python

    machine.action('Me','AddQuestion', '', _data={'title':..., 'topic_url_tokens':..., 'detail':..., 'is_anonymous':...})

Add Pin (发布想法)
------------------------------
You need to pass additional information as follows:

:code:`content` should be of form :code:`json.dumps([{'type':'text','content':'<p>xxxxxxx</p>'}])`, where 'xxxx' is your pin content.

.. code:: python

    machine.action('Me','AddPin', '', _data={'content':...})


Create Favorite List (创建收藏夹)
------------------------------------
You need to pass additional information as follows:

:code:`title` is a string containing the title.

:code:`description` is a string containing the description.

:code:`is_public` is a boolean.

.. code:: python

    machine.action('Me','CreateFavlist', '', _data={'title':..., 'description':..., 'is_public':...})

Report (举报)
---------------
You need to pass additional information as follows:

:code:`resource_id` is the ID of the content to report.

:code:`type` is a string, should be one of :code:`['answer', 'question', 'pin', 'article', 'comment', 'member']`

:code:`custom_reason` is a string containing the description when applicable, empty string otherwise.

:code:`reason_type` is a string. It has different sets of options for each category as listed. The items with (custom) means
that it requires a custom description. The "old" option corresponds to "others" in the visible list.

:Questions:
    ambiguity, subjective, rumour, abuse, provoke, medicine, personal, superstition, spam (custom), politics, porn, suicide, illegality (custom), old (custom).


:Answers and Articles:
    spam (custom), abuse, unfriendly (custom), politics,porn, untruth (custom), suicide, illegality (custom), repost (custom), temptation (custom), old (custom).


:Pins and Comments:
    spam (custom), abuse, unfriendly (custom), politics, porn, untruth (custom), suicide, illegality (custom), old (custom).


:Members:
    impersonate (custom), spam, profile (custom), old (custom).


Note: Reporting favorite lists is not included because it uses the old API.

.. code:: python

    machine.action('Me','Report', '', _data={'resource_id':..., 'type':..., 'reason_type':..., 'custom_reason':...})

Follow a User (关注用户)
------------------------------
.. code:: python

    machine.action('Members','Follow', user_url_token)

Unfollow a User (取消关注用户)
------------------------------
.. code:: python

    machine.action('Members','Unfollow', user_url_token)

Block a User (屏蔽用户)
------------------------------
.. code:: python

    machine.action('Members','Block', user_url_token)

Unblock a User (取消屏蔽用户)
------------------------------
.. code:: python

    machine.action('Members','Unblock', user_url_token)

Question Edit Topics (修改问题话题)
------------------------------------
You need to pass additional information as follows:

:code:`question` is a dict of format :code:`{'topic_url_tokens':['topic_id1','topic_id2']}`.

.. code:: python

    machine.action('Questions','EditTopics', question_id, _data={'question':...})


Question Edit Title (修改问题标题)
-----------------------------------
You need to pass additional information as follows:

:code:`question` is a dict of format :code:`{'title':'title_of_question'}`.

:code:`meta` is a dict of format :code:`{'reason':'标点或格式错误'}`.

.. code:: python

    machine.action('Questions','EditTitle', question_id, _data={'question':..., 'meta':...})

Question Edit Content (修改问题补充说明)
----------------------------------------
You need to pass additional information as follows:

:code:`question` is a dict of format :code:`{'title':'title_of_question', 'detail':'content_of_question'}`.

:code:`meta` is a dict of format :code:`{'reason':'标点或格式错误'}`.

.. code:: python

    machine.action('Questions','EditContent', question_id, _data={'question':..., 'meta':...})

Question Add Comment (评论问题)
---------------------------------
You need to pass additional information as follows:

:code:`content` is a string containing the comment.

:code:`reply_to_id` (optional) is a comment ID that you wish to reply to.

.. code:: python

    machine.action('Questions','AddComment', question_id, _data={'content':...})

Question Invite (邀请)
------------------------------
You need to pass additional information as follows:

:code:`member_hash` is the user hash of the invitee.

.. code:: python

    machine.action('Questions','Invite', question_id, _data={'member_hash':...})

Question Anonymize (启用匿名)
------------------------------
.. code:: python

    machine.action('Questions','Anonymize', question_id)

Question Deanonymize (取消匿名)
--------------------------------
.. code:: python

    machine.action('Questions','Deanonymize', question_id)

Question Add Answer (添加回答)
--------------------------------
You need to pass additional information as follows:

:code:`content` is a string containing the answer. The content should be wrapped with :code:`<p>xxxxx</p>`.

:code:`reshipment_settings` is a string. Its value should be one of :code:`['disallowed','allowed','need_payment']`.

:code:`comment_permission` is a string. Its value should be one of :code:`['all','censor','followee', or 'nobody']`.

.. code:: python

    machine.action('Questions','AddAnswer', question_id, _data={'content':..., 'reshipment_settings':..., 'comment_permission':...})

Delete Question (删除问题)
------------------------------
.. code:: python

    machine.action('Questions','DeleteQuestion', question_id)

Follow Question (关注问题)
------------------------------
.. code:: python

    machine.action('Questions','FollowQuestion', question_id)

Unfollow Question (取消关注问题)
----------------------------------
.. code:: python

    machine.action('Questions','UnfollowQuestion', question_id)

Answer Vote Up (点赞回答)
------------------------------
.. code:: python

    machine.action('Answers','VoteUp', answer_id)

Answer Cancel Vote (取消点赞/反对回答)
--------------------------------------
.. code:: python

    machine.action('Answers','CancelVote', answer_id)

Answer Vote Down (反对回答)
------------------------------
.. code:: python

    machine.action('Answers','VoteDown', answer_id)

Answer Add Comment (评论回答)
------------------------------
You need to pass additional information as follows:

:code:`content` is a string containing the comment.

.. code:: python

    machine.action('Answers','AddComment', answer_id, _data={'content':...})

Answer Thank (感谢回答)
------------------------------
.. code:: python

    machine.action('Answers','Thank', answer_id)

Answer Undo Thank (取消感谢回答)
---------------------------------
.. code:: python

    machine.action('Answers','UndoThank', answer_id)

Answer Mark Unhelpful (没有帮助)
-----------------------------------
.. code:: python

    machine.action('Answers','MarkUnhelpful', answer_id)

Answer Undo Mark Unhelpful (取消没有帮助)
-------------------------------------------
.. code:: python

    machine.action('Answers','UndoMarkUnhelpful', answer_id)

Answer Set Comment Permission (修改回答评论权限)
-------------------------------------------------
You need to pass additional information as follows:

:code:`comment_permission` is a string. Its value should be one of :code:`['all','censor','followee', or 'nobody']`.

.. code:: python

    machine.action('Answers','SetCommentPermission', answer_id, _data={'comment_permission':...})

Answer Set Reshipment Permission (修改回答转载设置)
------------------------------------------------------
You need to pass additional information as follows:

:code:`reshipment_settings` is a string. Its value should be one of :code:`['disallowed','allowed','need_payment']`.

.. code:: python

    machine.action('Answers','SetReshipmentPermission', answer_id, _data={'reshipment_settings':...})

Edit Answer (修改回答)
------------------------------
You need to pass additional information as follows:

:code:`content` is a string containing the answer. The content should be wrapped with :code:`<p>xxxxx</p>`.

.. code:: python

    machine.action('Answers','EditAnswer', answer_id, _data={'content':...})

Delete Answer (删除回答)
------------------------------
.. code:: python

    machine.action('Answers','DeleteAnswer', answer_id)

Restore Answer (撤销删除回答)
------------------------------
.. code:: python

    machine.action('Answers','RestoreAnswer', answer_id)

Delete Comment (删除评论)
------------------------------
.. code:: python

    machine.action('Comments','DeleteComment', comment_id)

Like Comment (点赞评论)
------------------------------
.. code:: python

    machine.action('Comments','LikeComment', comment_id)

Undo Like Comment (取消点赞评论)
---------------------------------
.. code:: python

    machine.action('Comments','UndoLikeComment', comment_id)

Dislike Comment (踩评论)
------------------------------
.. code:: python

    machine.action('Comments','DislikeComment', comment_id)

Undo Dislike Comment (取消踩评论)
-----------------------------------
.. code:: python

    machine.action('Comments','UndoDislikeComment', comment_id)

Feature Comment (设为推荐评论)
------------------------------
.. code:: python

    machine.action('Comments','Feature', comment_id)

Undo Feature Comment (取消推荐评论)
------------------------------------
.. code:: python

    machine.action('Comments','UndoFeature', comment_id)

Collapse Comment (折叠评论)
------------------------------
.. code:: python

    machine.action('Comments','Collapse', comment_id)

Undo Collapse Comment (取消折叠评论)
------------------------------------
.. code:: python

    machine.action('Comments','UndoCollapse', comment_id)

Pin Add Comment (评论想法)
------------------------------
You need to pass additional information as follows:

:code:`content` is a string containing the comment.

:code:`reply_to_id` (optional) is a comment ID that you wish to reply to.

.. code:: python

    machine.action('Pins','AddComment', pin_id, _data={'content':...})

Pin Like (鼓掌想法)
------------------------------
.. code:: python

    machine.action('Pins','Like', pin_id)

Pin Undo Like (取消鼓掌想法)
------------------------------
.. code:: python

    machine.action('Pins','UndoLike', pin_id)

Delete Pin (删除想法)
------------------------------
.. code:: python

    machine.action('Pins','DeletePin', pin_id)

Follow Topic (关注话题)
------------------------------
.. code:: python

    machine.action('Topics','FollowTopic', topic_id)

Unfollow Topic (取消关注话题)
------------------------------
.. code:: python

    machine.action('Topics','UnfollowTopic', topic_id)

Favorite Lists Add Entry (收藏回答/文章/想法)
---------------------------------------------
You need to pass additional information as follows:

:code:`content_id` is the ID of the answer/article/pin.

:code:`content_type` is a string, it should be one of :code:`['answer', 'pin' or 'article']`.

.. code:: python

    machine.action('Favlists','AddEntry', favlist_id, _data={'content_id':..., 'content_type':...})

Favorite Lists Add Comment (评论收藏夹)
----------------------------------------
You need to pass additional information as follows:

:code:`content` is a string containing the comment.

:code:`reply_to_id` (optional) is a comment ID that you wish to reply to.

.. code:: python

    machine.action('Favlists','AddComment', favlist_id, _data={'content':...})

Follow Favorite Lists (关注收藏夹)
-------------------------------------
You need to pass additional information as follows:

:code:`favlist_id` is the ID of the favorite list.

Please note that this inconsistency is caused by version difference of Zhihu API. This action uses the old
form version instead of v4 API.

.. code:: python

    machine.action('Favlists','FollowFavlist', '', _data={'favlist_id':...})

Follow Column (关注专栏)
------------------------------
.. code:: python

    machine.action('Columns','FollowColumn', column_id)

Unfollow Column (取消关注专栏)
------------------------------
.. code:: python

    machine.action('Columns','UnfollowColumn', column_id)

Article Add Comment (评论文章)
------------------------------
You need to pass additional information as follows:

:code:`content` is a string containing the comment.

:code:`reply_to_id` (optional) is a comment ID that you wish to reply to.

.. code:: python

    machine.action('Articles','AddComment', article_id, _data={'content':...})

Article Set Comment Permission (修改文章评论权限)
---------------------------------------------------
You need to pass additional information as follows:

:code:`comment_permission` is a string. Its value should be one of :code:`['all','censor','followee', or 'nobody']`.

.. code:: python

    machine.action('Articles','SetCommentPermission', article_id, _data={'comment_permission':...})

Delete Article (删除文章)
------------------------------
.. code:: python

    machine.action('Articles','DeleteArticle', article_id)

Article Vote Up (点赞文章)
------------------------------
.. code:: python

    machine.action('Articles','VoteUp', article_id)

Article Cancel Vote (取消点赞文章)
------------------------------------
.. code:: python

    machine.action('Articles','CancelVote', article_id)

