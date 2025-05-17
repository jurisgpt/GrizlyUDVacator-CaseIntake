import streamlit as st
from bs4 import BeautifulSoup
import pytest
import re

# HTML content from external_form_tab.py
def get_form_html():
    return """
    <section class="form-container" style="text-align: center; margin: 20px 0;">
        <iframe 
            src="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true" 
            width="640" 
            height="1544" 
            frameborder="0" 
            marginheight="0" 
            marginwidth="0" 
            allowfullscreen="allowfullscreen"
            title="Tenant Relief Evaluation Form"
            aria-label="Tenant Relief Evaluation Form"
            role="application">
            <p>Your browser does not support iframes. Please visit the 
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform" 
                   rel="noopener noreferrer" 
                   target="_blank">form directly</a>.</p>
        </iframe>
    </section>
    """

def test_html_structure():
    """Test HTML structure and nesting"""
    soup = BeautifulSoup(get_form_html(), 'html.parser')
    
    # Check root element
    assert soup.section is not None
    assert soup.section.get('class') == ['form-container']
    
    # Check iframe
    iframe = soup.iframe
    assert iframe is not None
    assert iframe.parent.name == 'section'
    
    # Check fallback content
    assert iframe.p is not None
    assert iframe.p.a is not None

def test_html_attributes():
    """Test HTML attributes and their values"""
    soup = BeautifulSoup(get_form_html(), 'html.parser')
    iframe = soup.iframe
    
    # Check required attributes
    required_attrs = {
        'src': re.compile(r'https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform'),
        'width': '640',
        'height': '1544',
        'frameborder': '0',
        'marginheight': '0',
        'marginwidth': '0',
        'allowfullscreen': 'allowfullscreen',
        'title': 'Tenant Relief Evaluation Form',
        'aria-label': 'Tenant Relief Evaluation Form',
        'role': 'application'
    }
    
    for attr, expected in required_attrs.items():
        assert attr in iframe.attrs
        value = iframe[attr]
        if isinstance(expected, re.Pattern):
            assert expected.match(value)
        else:
            assert value == expected

def test_link_attributes():
    """Test link attributes for security and accessibility"""
    soup = BeautifulSoup(get_form_html(), 'html.parser')
    link = soup.find('a')
    
    assert link is not None
    assert link['href'].startswith('https://')
    assert link['rel'] == ['noopener', 'noreferrer']
    assert link['target'] == '_blank'

def test_html_semantics():
    """Test semantic HTML structure"""
    soup = BeautifulSoup(get_form_html(), 'html.parser')
    
    # Check semantic container
    assert soup.section is not None
    assert soup.section.get('class') == ['form-container']
    
    # Check proper nesting
    iframe = soup.iframe
    assert iframe.parent.name == 'section'
    assert iframe.p is not None
    assert iframe.p.parent == iframe

def test_html_accessibility():
    """Test accessibility attributes"""
    soup = BeautifulSoup(get_form_html(), 'html.parser')
    iframe = soup.iframe
    
    # Check ARIA attributes
    assert 'aria-label' in iframe.attrs
    assert iframe['aria-label'] == 'Tenant Relief Evaluation Form'
    assert 'role' in iframe.attrs
    assert iframe['role'] == 'application'
    
    # Check title attribute
    assert 'title' in iframe.attrs
    assert iframe['title'] == 'Tenant Relief Evaluation Form'

if __name__ == '__main__':
    pytest.main([__file__])
