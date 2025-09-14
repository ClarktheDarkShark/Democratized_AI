import Layout from '../components/Layout';
import ApprovalQueue from '../components/ApprovalQueue';

export default function ApprovalsPage() {
  return (
    <Layout>
      <h1>Approvals</h1>
      <ApprovalQueue />
    </Layout>
  );
}
