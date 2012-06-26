from django import template
from github import Github
import markdown
import re
from hashlib import md5

register = template.Library()

def gfm(text):
    # Extract pre blocks.
    extractions = {}
    def pre_extraction_callback(matchobj):
        digest = md5(matchobj.group(0)).hexdigest()
        extractions[digest] = matchobj.group(0)
        return "{gfm-extraction-%s}" % digest
    pattern = re.compile(r'<pre>.*?</pre>', re.MULTILINE | re.DOTALL)
    text = re.sub(pattern, pre_extraction_callback, text)

    # Prevent foo_bar_baz from ending up with an italic word in the middle.
    def italic_callback(matchobj):
        s = matchobj.group(0)
        if list(s).count('_') >= 2:
            return s.replace('_', '\_')
        return s
    text = re.sub(r'^(?! {4}|\t)\w+_\w+_\w[\w_]*', italic_callback, text)

    # In very clear cases, let newlines become <br /> tags.
    def newline_callback(matchobj):
        if len(matchobj.group(1)) == 1:
            return matchobj.group(0).rstrip() + '  \n'
        else:
            return matchobj.group(0)
    pattern = re.compile(r'^[\w\<][^\n]*(\n+)', re.MULTILINE)
    text = re.sub(pattern, newline_callback, text)

    # Insert pre block extractions.
    def pre_insert_callback(matchobj):
        return '\n\n' + extractions[matchobj.group(1)]
    text = re.sub(r'{gfm-extraction-([0-9a-f]{32})\}', pre_insert_callback, text)

    return text

def github_org(organization):
    github = Github()
    org = github.get_organization(organization)
    team = "<p>emit the markup for all Github org %s</p>" % (organization)
    return team

def github_repos(organization):
    github = Github()
    org = github.get_organization(organization)
    team = "<p>emit the markup for all of the public repositories of %s in Github</p>" % (organization)
    return team

def get_bio_html(bio, login, truncated=True):
    # Force to string
    bio_str = "%s" % (bio)

    if truncated:
        # Truncate to 255 characters
        bio_str = bio_str[:255] if len(bio_str) > 255 else bio_str

        # Make sure we don't truncate in the middle of a word 
        left, splitter, right = bio_str.rpartition(" ")

        # Now handle the case where there is only one paragraph in the first 300 characters.
        bio_markdown = left + " (<a href=\"" + login + "\">Read more...</a>)" if len(left) > 0 else right
    else:
        bio_markdown = bio_str

    # Convert markdown to HTML and return
    return markdown.markdown(gfm(bio_markdown))

def get_avatar_html(avatar, size):
    avatar_html = "<ul class=\"thumbnails\">"
    avatar_html += "<li class=\"span2\">"
    avatar_html += "<div class=\"thumbnail\">"
    avatar_html += "<img src=\"%s&s=%d\" width=\"%d\" height=\"%d\" />" % (avatar, size, size, size)
    avatar_html += "</div></li></ul>"
    return avatar_html

def github_members(organization, size=200):
    github = Github()
    org = github.get_organization(organization)
    members = org.get_members()

    team_html = ""
    for member in members:
        avatar_html = get_avatar_html(member.avatar_url, size)
        name_html = "<strong>%s</strong>" % (member.name)
        bio_html = get_bio_html(member.bio, member.login, True)
        team_html += "<div class=\"row\"><div class=\"span2\">" + avatar_html + "</div><div class=\"span4\">" + name_html + bio_html + "</div></div>"

    return team_html

def github_user(login, size=200):
    github = Github()
    user = github.get_user(login)

    avatar_html = get_avatar_html(user.avatar_url, size)
    bio_html = get_bio_html(user.bio, user.login, False)
    user_html = "<div class=\"row\"><div class=\"span2\">" + avatar_html + "</div><div class=\"span4\">" + bio_html + "</div></div>"
    return user_html

def github_user_name(login):
    github = Github()
    user = github.get_user(login)
    return "%s" % (user.name)

register.simple_tag(github_org)
register.simple_tag(github_repos)
register.simple_tag(github_members)
register.simple_tag(github_user)
register.simple_tag(github_user_name)
