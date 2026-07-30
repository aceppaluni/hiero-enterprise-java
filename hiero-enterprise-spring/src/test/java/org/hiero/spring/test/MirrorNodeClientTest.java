package org.hiero.spring.test;

import java.util.List;
import org.hiero.base.HieroException;
import org.hiero.base.data.Node;
import org.hiero.base.mirrornode.MirrorNodeClient;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest(classes = HieroTestConfig.class)
public class MirrorNodeClientTest {

  @Autowired private MirrorNodeClient mirrorNodeClient;

  @Test
  @Disabled("Verified against testnet; disabled because CI cannot access testnet")
  void findNetworkNodes() throws HieroException {
    List<Node> result = mirrorNodeClient.queryNetworkNodes().getData();

    Assertions.assertNotNull(result);
    Assertions.assertFalse(result.isEmpty());

    Node node = result.getFirst();

    Assertions.assertNotNull(node);
    Assertions.assertNotNull(node.nodeId());
  }
}
