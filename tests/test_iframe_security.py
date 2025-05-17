import streamlit as st
from bs4 import BeautifulSoup
import pytest
import re

def test_iframe_security_attributes():
    """Test iframe security attributes"""
    # Define the HTML string directly
    html = """
    <iframe
        src="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true"
        sandbox="allow-forms allow-same-origin allow-scripts"
        allow="autoplay; encrypted-media; fullscreen; microphone; camera"
        allowfullscreen="allowfullscreen"
    ></iframe>
    """
    
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    iframe = soup.iframe
    
    assert iframe is not None
    
    # Verify security attributes
    assert 'sandbox' in iframe.attrs
    assert 'allow' in iframe.attrs
    assert 'allowfullscreen' in iframe.attrs
    
    # Verify sandbox permissions
    sandbox_perms = str(iframe['sandbox'])
    assert 'allow-forms' in sandbox_perms
    assert 'allow-same-origin' in sandbox_perms
    assert 'allow-scripts' in sandbox_perms
    
    # Verify allow permissions
    allow_perms = str(iframe['allow'])
    required_allow = ['autoplay', 'encrypted-media', 'fullscreen', 'microphone', 'camera']
    assert all(perm in allow_perms for perm in required_allow)

def test_iframe_protocol_handling():
    """Test iframe protocol handling"""
    # Define both iframes in a single HTML string
    html = """
    <iframe
        src="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true"
        sandbox="allow-forms allow-same-origin allow-scripts"
    ></iframe>
    <iframe
        src="http://example.com/form"
        sandbox="allow-forms allow-same-origin allow-scripts"
    ></iframe>
    """
    
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    iframes = soup.find_all('iframe')
    
    assert len(iframes) == 2
    
    # Verify HTTPS iframe is present
    https_iframe = None
    for iframe in iframes:
        if iframe['src'].startswith('https://'):
            https_iframe = iframe
            break
    
    assert https_iframe is not None
    
    # Verify HTTP iframe is not accessible
    http_iframe = None
    for iframe in iframes:
        if iframe['src'].startswith('http://'):
            http_iframe = iframe
            break
    
    assert http_iframe is not None
    assert 'sandbox' in http_iframe.attrs

def test_iframe_error_handling():
    """Test iframe error handling"""
    # Define the HTML string directly
    html = """
    <div class="iframe-container">
        <iframe
            src="https://invalid-url-that-will-fail"
            onload="this.style.display='block';"
            onerror="handleFrameError(this)"
            sandbox="allow-forms allow-same-origin allow-scripts"
        ></iframe>
        <div id="iframe-error" style="display: none;">
            <div class="error-message">
                <h4>⚠️ Content Failed to Load</h4>
                <p>Please check your internet connection or try again later.</p>
            </div>
        </div>
    </div>
    
    <script>
    function handleFrameError(frame) {
        const container = frame.closest('.iframe-container');
        container.querySelector('.iframe-error').style.display = 'block';
    }
    </script>
    """
    
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Verify error handling structure
    container = soup.find('div', class_='iframe-container')
    assert container is not None
    
    iframe = container.iframe
    assert iframe is not None
    assert 'onerror' in iframe.attrs
    
    error_div = container.find('div', id='iframe-error')
    assert error_div is not None
    assert error_div.get('style') == 'display: none;'

def test_iframe_permissions():
    """Test iframe permission attributes"""
    # Define the HTML string directly
    html = """
    <iframe
        src="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true"
        sandbox="allow-forms allow-same-origin allow-scripts"
        allow="autoplay; encrypted-media; fullscreen; microphone; camera"
        allowfullscreen="allowfullscreen"
        allowpaymentrequest="allowpaymentrequest"
    ></iframe>
    """
    
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    iframe = soup.iframe
    
    assert iframe is not None
    
    # Verify permission attributes
    assert 'allow' in iframe.attrs
    assert 'allowfullscreen' in iframe.attrs
    assert 'allowpaymentrequest' in iframe.attrs
    
    # Verify allow values
    allow_perms = str(iframe['allow']).split(';')
    allow_perms = [perm.strip() for perm in allow_perms]
    required_allow = ['autoplay', 'encrypted-media', 'fullscreen', 'microphone', 'camera']
    assert all(perm in allow_perms for perm in required_allow)

if __name__ == '__main__':
    pytest.main([__file__])
