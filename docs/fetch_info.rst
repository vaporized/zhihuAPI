.. _fetch_info:

Fetching Information
====================
This section lists APIs that fetches information with GET, all calls are not visible to other Zhihu users (excluding 知乎管理员).
Assuming you have created an instance:

.. code:: python

    from zhihuAPI.account import ZhihuAccount
    machine = ZhihuAccount('path/to/cookie.json')

All code examples uses :code:`get_all_pages_json`, it can be replaced with :code:`save_all_pages_json`.

My Information (账号信息)
--------------------------
.. code:: python

    machine.get_all_pages_json('Miscellaneous','Me','')


User Information (用户信息)
---------------------------
.. code:: python

    machine.get_all_pages_json('Miscellaneous','Profile', user_url_token)


Topic Information (话题信息)
----------------------------
.. code:: python

    machine.get_all_pages_json('Miscellaneous','Topic', topic_id)


Question Information (问题信息)
--------------------------------
.. code:: python

    machine.get_all_pages_json('Miscellaneous','Question', question_id)


Answer Information (回答信息)
--------------------------------
.. code:: python

    machine.get_all_pages_json('Miscellaneous','Answer', answer_id)


Preview of Messages (私信预览)
-------------------------------
.. code:: python

    machine.get_all_pages_json('Miscellaneous','Messages', '')

Notifications (通知)
------------------------------
.. code:: python

    machine.get_all_pages_json('Miscellaneous','Notifications', '')

Followees (关注的人)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Followees', user_url_token)

Followers (关注者)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Followers', user_url_token)

Following Questions (关注的问题)
---------------------------------
.. code:: python

    machine.get_all_pages_json('Members','FollowingQuestions', user_url_token)

Following Topics (关注的话题)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','FollowingTopics', user_url_token)

Following Columns (关注的专栏)
-------------------------------
.. code:: python

    machine.get_all_pages_json('Members','FollowingColumns', user_url_token)

Following Favorite Lists (关注的收藏夹)
---------------------------------------
.. code:: python

    machine.get_all_pages_json('Members','FollowingFavlists', user_url_token)

Questions (提问)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Questions', user_url_token)

Answers (回答)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Answers', user_url_token)

Pins (想法)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Pins', user_url_token)

Articles (文章)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Articles', user_url_token)

Columns (专栏)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Columns', user_url_token)

Favorite Lists (收藏)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Favlists', user_url_token)

Activities (动态)
------------------------------
.. code:: python

    machine.get_all_pages_json('Members','Activities', user_url_token)

Question Followers (问题关注者)
---------------------------------
.. code:: python

    machine.get_all_pages_json('Questions','Followers', question_id)

Question Comments (问题评论)
-------------------------------
.. code:: python

    machine.get_all_pages_json('Questions','Comments', question_id)

Question Invitees (被邀请的人)
--------------------------------
.. code:: python

    machine.get_all_pages_json('Questions','Invitees', question_id)

Question Invitation Candidates (可能被邀请的人)
-------------------------------------------------
.. code:: python

    machine.get_all_pages_json('Questions','InvitationCandidates', question_id)

Similar Questions (相关问题)
-------------------------------
.. code:: python

    machine.get_all_pages_json('Questions','SimilarQuestions', question_id)

Question Meta Related Topics
------------------------------
.. code:: python

    machine.get_all_pages_json('Questions','MetaRelatedTopics', question_id)

Question Related Knowledge Commodities (问题相关推荐)
-------------------------------------------------------
.. code:: python

    machine.get_all_pages_json('Questions','RelatedKnowledgeCommodities', question_id)

Answer Upvoters (回答点赞者)
------------------------------
.. code:: python

    machine.get_all_pages_json('Answers','Upvoters', answer_id)

Answer Comments (回答评论)
------------------------------
.. code:: python

    machine.get_all_pages_json('Answers','Comments', answer_id)

Comments With Conversation (包含某评论的对话)
----------------------------------------------
.. code:: python

    machine.get_all_pages_json('Comments','CommentsWithConversation', comment_id)

Pin Comments (想法评论)
------------------------------
.. code:: python

    machine.get_all_pages_json('Pins','Comments', pin_id)

Topic Followers (话题关注者)
------------------------------
.. code:: python

    machine.get_all_pages_json('Topics','Followers', topic_id)

Topic Essence (话题精华)
------------------------------
.. code:: python

    machine.get_all_pages_json('Topics','Essence', topic_id)

Topic Top Questions (话题精华问题)
------------------------------------
.. code:: python

    machine.get_all_pages_json('Topics','TopQuestions', topic_id)

Topic Timeline Questions (话题最新问题)
-----------------------------------------
.. code:: python

    machine.get_all_pages_json('Topics','TimelineQuestions', topic_id)

Topic Best Answerers (话题优秀答主)
--------------------------------------
.. code:: python

    machine.get_all_pages_json('Topics','BestAnswerers', topic_id)

Topic Top Activities (话题精华动态)
-------------------------------------
.. code:: python

    machine.get_all_pages_json('Topics','TopActivities', topic_id)

Topic Timeline Activities (话题最新动态)
------------------------------------------
.. code:: python

    machine.get_all_pages_json('Topics','TimelineActivities', topic_id)

Article Upvoters (文章点赞者)
--------------------------------
.. code:: python

    machine.get_all_pages_json('Articles','Upvoters', article_id)

Article Comments (文章评论)
------------------------------
.. code:: python

    machine.get_all_pages_json('Articles','Comments', article_id)

Column Followers (专栏关注者)
------------------------------
.. code:: python

    machine.get_all_pages_json('Columns','Followers', column_id)

Column Posts (专栏文章)
------------------------------
.. code:: python

    machine.get_all_pages_json('Columns','Posts', column_id)


Other Features
-------------------
These features are not usages of Zhihu APIs, they exist for historical reasons, and maybe removed in the future.

Save to HTML
^^^^^^^^^^^^^^^^
This function saves static html pages. :code:`item` can be set to :code:`'Questions'`, :code:`'Answers'`
or :code:`Articles` to save all the corresponding contents of a certain user. Pictures are not downloaded, and
scripts tags are removed in the saved pages to prevent a page flashing bug caused by relative path script loading.

.. code:: python

    machine.save_all_html(item, user_url_token, save_path)

