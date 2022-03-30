import pytest
import filecmp
import web_blocker as wb


def test_get_block_list():
    '''Test that method get block list successfully store the whole blocked sites text file to an array'''
    parsed_file = 'temporarily_block_site.txt'
    block_list = wb.get_block_list(parsed_file)

    #write content of the block_list array to a test text file
    with open("test_get_block_list.txt", "w") as test_file:
        for site in block_list:
            test_file.write("".join(site) + "\n")

    #Compare original text file with the test text file
    result = filecmp.cmp('temporarily_block_site.txt', 'test_get_block_list.txt')
    assert result

def test_block_websites_temporarily():
    wb.block_websites_temporarily(1,23)

    block_list = wb.get_block_list('temporarily_block_site.txt')

    #Check that every site in the blocked list is included in /etc/host file
    with open('/etc/hosts', 'r') as hf:
        hosts_content = hf.read()
        for site in block_list:
            assert site in hosts_content

def test_block_websites_permanently():
    wb.block_websites_permanently()

    block_list = wb.get_block_list('permanently_block_site.txt')

    #Check that every site in the blocked list is included in /etc/host file
    with open('/etc/hosts', 'r') as hf:
        hosts_content = hf.read()
        for site in block_list:
            assert site in hosts_content


def test_unblock_websites_temporarily():
    wb.unblock_list_of_temporary()

    block_list = wb.get_block_list('temporarily_block_site.txt')

    #Check that every site in the blocked list is no longer included in /etc/host file
    with open('/etc/hosts', 'r') as hf:
        hosts_content = hf.read()
        for site in block_list:
            assert site not in hosts_content
